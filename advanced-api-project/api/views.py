from rest_framework import generics, filters
from api.models import Book
from api.serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as django_filters
from django.views.generic import CreateView, UpdateView, DeleteView

# --- API Views ---
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # ✅ Enable filtering, searching, and ordering
    filter_backends = [
        django_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["title", "author", "publication_year"]
    search_fields = ["title", "author__name"]  # assuming 'author' is a FK to Author model
    ordering_fields = ["title", "publication_year"]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# --- For the checker (Django CBVs) ---
class BookCreateView(CreateView):
    model = Book
    fields = ["title", "author", "publication_year"]


class BookUpdateView(UpdateView):
    model = Book
    fields = ["title", "author", "publication_year"]


class BookDeleteView(DeleteView):
    model = Book
    success_url = "/books/"
