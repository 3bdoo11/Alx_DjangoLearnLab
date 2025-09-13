from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from django.http import HttpResponseForbidden

from .models import Book, Library


# ========== AUTH ==========
def register(request):
    """ Register a new user """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# ========== LIBRARY ==========
def list_books(request):
    """ Show all books """
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    """ Show library detail """
    model = Library
    template_name = "relationship_app/library_detail.html"


# ========== ROLE-BASED ==========
@login_required
def admin_view(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Admins only!")
    return render(request, "relationship_app/admin_view.html")


@login_required
def librarian_view(request):
    if not request.user.groups.filter(name="Librarians").exists():
        return HttpResponseForbidden("Librarians only!")
    return render(request, "relationship_app/librarian_view.html")


@login_required
def member_view(request):
    if not request.user.groups.filter(name="Members").exists():
        return HttpResponseForbidden("Members only!")
    return render(request, "relationship_app/member_view.html")


# ========== BOOK MANAGEMENT ==========
@login_required
@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author")
        if title and author_id:
            Book.objects.create(title=title, author_id=author_id)
            return redirect("list_books")
    return render(request, "relationship_app/add_book.html")


@login_required
@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title", book.title)
        book.author_id = request.POST.get("author", book.author_id)
        book.save()
        return redirect("list_books")
    return render(request, "relationship_app/edit_book.html", {"book": book})


@login_required
@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})
