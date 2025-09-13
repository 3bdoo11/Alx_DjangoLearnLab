from django.urls import path
from . import views

urlpatterns = [
    # existing views
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # authentication
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # role-based views
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),

    # book management with custom permissions
    path("books/add_book/", views.add_book, name="add_book"),          
    path("books/edit_book/<int:book_id>/", views.edit_book, name="edit_book"),  
    path("books/delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
]
