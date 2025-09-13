# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser, Book, Library

# # ===========================
# # Custom User Admin
# # ===========================
# class CustomUserAdmin(UserAdmin):
#     # الحقول اللي هتظهر في صفحة تفاصيل المستخدم
#     fieldsets = (
#         (None, {"fields": ("username", "password")}),
#         ("Personal info", {"fields": ("first_name", "last_name", "email", "date_of_birth", "profile_photo")}),
#         (
#             "Permissions",
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 )
#             },
#         ),
#         ("Important dates", {"fields": ("last_login", "date_joined")}),
#     )

#     # الحقول اللي تظهر عند إنشاء مستخدم جديد
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("username", "email", "date_of_birth", "profile_photo", "password1", "password2"),
#             },
#         ),
#     )

#     list_display = ("username", "email", "first_name", "last_name", "date_of_birth", "is_staff")
#     search_fields = ("username", "email", "first_name", "last_name")
#     ordering = ("username",)


# # ===========================
# # Book Admin
# # ===========================
# class BookAdmin(admin.ModelAdmin):
#     list_display = ("title", "author", "published_date", "isbn", "added_by")
#     search_fields = ("title", "author", "isbn")
#     list_filter = ("published_date",)


# # ===========================
# # Library Admin
# # ===========================
# class LibraryAdmin(admin.ModelAdmin):
#     list_display = ("name", "location")
#     search_fields = ("name", "location")


# # ===========================
# # Register models
# # ===========================
# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Book, BookAdmin)
# admin.site.register(Library, LibraryAdmin)
