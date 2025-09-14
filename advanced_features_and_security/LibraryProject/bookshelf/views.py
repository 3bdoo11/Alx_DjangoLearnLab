from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods
from .models import Book
from .forms import BookForm, ExampleForm  # ✅ استيراد كلا النموذجين

# ========================
# Book Views with Permissions
# ========================

@login_required
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # ORM يحمي من SQL injection
    return render(request, "bookshelf/book_list.html", {"books": books})

@login_required
@permission_required("bookshelf.can_create", raise_exception=True)
@require_http_methods(["GET", "POST"])
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/create_book.html", {"form": form})

@login_required
@permission_required("bookshelf.can_edit", raise_exception=True)
@require_http_methods(["GET", "POST"])
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/edit_book.html", {"form": form, "book": book})

@login_required
@permission_required("bookshelf.can_delete", raise_exception=True)
@require_http_methods(["POST"])
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("book_list")

# ========================
# ExampleForm View (لأغراض الاختبار/ALX)
# ========================
@login_required
@require_http_methods(["GET", "POST"])
def example_view(request):
    """
    View لاستخدام ExampleForm لأغراض التدريب أو الاختبار.
    """
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = ExampleForm()
    return render(request, "bookshelf/example_form.html", {"form": form})
