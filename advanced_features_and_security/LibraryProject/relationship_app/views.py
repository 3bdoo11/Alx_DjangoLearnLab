from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Book
from bookshelf.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

# --- Basic views ---
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/book_list.html", {"books": books})


from django.views.generic import DetailView

class LibraryDetailView(DetailView):
    model = Book
    template_name = "relationship_app/library_detail.html"
    context_object_name = "book"


# --- Authentication ---
def login_view(request):
    # custom login logic
    return render(request, "relationship_app/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# --- Role-based views ---
@login_required
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@login_required
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@login_required
def member_view(request):
    return render(request, "relationship_app/member_view.html")


# --- Book management ---
@login_required
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        published_date = request.POST.get("published_date")
        Book.objects.create(title=title, author=author, published_date=published_date, added_by=request.user)
        return redirect("list_books")
    return render(request, "relationship_app/add_book.html")


@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.published_date = request.POST.get("published_date")
        book.save()
        return redirect("list_books")
    return render(request, "relationship_app/edit_book.html", {"book": book})


@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect("list_books")

def home(request):
    return render(request, "relationship_app/home.html")
