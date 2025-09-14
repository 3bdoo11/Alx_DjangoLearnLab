from django.contrib import admin
from .models import Author, Library, Librarian  # ✅ شيل Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    search_fields = ("name",)


@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ("user", "library")
    search_fields = ("user__username", "library__name")
