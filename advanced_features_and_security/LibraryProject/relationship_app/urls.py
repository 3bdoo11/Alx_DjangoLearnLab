from django.urls import path
from . import views

urlpatterns = [
    # --- Home ---
    path("", views.home, name="home"),

    # --- Authentication ---
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),

    # --- Role-based views ---
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),

    # --- Book views ---
    path("books/", views.list_books, name="list_books"),
    path("books/<int:pk>/", views.LibraryDetailView.as_view(), name="book_detail"),
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:book_id>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:book_id>/delete/", views.delete_book, name="delete_book"),
]
