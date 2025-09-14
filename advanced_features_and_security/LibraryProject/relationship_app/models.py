from django.db import models
from django.conf import settings
from bookshelf.models import Book  

# --- Author model ---
class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# --- Library model ---
class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, blank=True)  # ربط الكتب

    def __str__(self):
        return self.name


# --- Librarian model ---
class Librarian(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.library.name}"
