from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from api.models import Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")

        # Create some initial books
        self.book1 = Book.objects.create(title="Book A", author="Author X", publication_year=2020)
        self.book2 = Book.objects.create(title="Book B", author="Author Y", publication_year=2021)

        self.list_url = reverse("book-list")  # Should match your viewset/urls name

    def test_create_book(self):
        data = {"title": "New Book", "author": "New Author", "publication_year": 2024}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=response.data["id"]).title, "New Book")

    def test_get_books_list(self):
        response = self.client.get(self.list_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        data = {"title": "Updated Title", "author": "Author X", "publication_year": 2022}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        url = reverse("book-detail", args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + "?author=Author X")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Author X")

    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=Book A")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Book A")

    def test_order_books_by_year(self):
        response = self.client.get(self.list_url + "?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data[0]["publication_year"] <= response.data[1]["publication_year"])

    def test_unauthenticated_access_denied(self):
        self.client.logout()
        response = self.client.post(self.list_url, {"title": "Fail Book"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
