# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.db import models
# from django.urls import reverse


# # ===========================
# # Custom User Manager
# # ===========================
# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, email=None, password=None, **extra_fields):
#         """
#         Create and return a regular user with email, username and password.
#         """
#         if not username:
#             raise ValueError("The Username field is required")
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email=None, password=None, **extra_fields):
#         """
#         Create and return a superuser with admin permissions.
#         """
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_active", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")

#         return self.create_user(username, email, password, **extra_fields)


# # ===========================
# # Custom User Model
# # ===========================
# class CustomUser(AbstractUser):
#     date_of_birth = models.DateField(null=True, blank=True)
#     profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

#     objects = CustomUserManager()  # ربط الموديل بالـ Manager

#     def __str__(self):
#         return self.username


# # ===========================
# # Book Model
# # ===========================
# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=200)
#     published_date = models.DateField()
#     isbn = models.CharField(max_length=13, unique=True)
#     added_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="added_books")

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse("book_detail", kwargs={"pk": self.pk})


# # ===========================
# # Library Model
# # ===========================
# class Library(models.Model):
#     name = models.CharField(max_length=200)
#     location = models.CharField(max_length=200)
#     books = models.ManyToManyField(Book, related_name="libraries")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("library_detail", kwargs={"pk": self.pk})
