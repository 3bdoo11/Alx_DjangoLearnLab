from django.contrib import admin
from .models import Author, Book, Library, Librarian

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "added_by")
    list_filter = ("published_date", "author")
    search_fields = ("title",)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    search_fields = ("name",)


@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ("user", "library")
    search_fields = ("user__username", "library__name")
