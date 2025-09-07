from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # existing views
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # authentication
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),

    # role-based views
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),

    # book management with custom permissions
    path("books/add_book/", views.add_book, name="add_book"),          
    path("books/edit_book/<int:book_id>/", views.edit_book, name="edit_book"),  
    path("books/delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
]
