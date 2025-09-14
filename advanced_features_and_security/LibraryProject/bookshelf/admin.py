from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser, Book


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        "username", "email", "first_name", "last_name",
        "date_of_birth", "profile_photo_preview", "is_staff"
    )
    list_filter = ("is_staff", "is_superuser", "is_active")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": (
            "first_name", "last_name", "email",
            "date_of_birth", "profile_photo"
        )}),
        ("Permissions", {"fields": (
            "is_active", "is_staff", "is_superuser",
            "groups", "user_permissions"
        )}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "password1", "password2",
                "date_of_birth", "profile_photo", "is_staff", "is_active"
            ),
        }),
    )

    search_fields = ("username", "email")
    ordering = ("username",)

    def profile_photo_preview(self, obj):
        if obj.profile_photo:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:50%;" />',
                obj.profile_photo.url
            )
        return "No Photo"
    profile_photo_preview.short_description = "Profile Photo"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "isbn", "added_by")
    search_fields = ("title", "author", "isbn")
    list_filter = ("published_date",)

    def has_view_permission(self, request, obj=None):
        return request.user.has_perm("bookshelf.can_view")

    def has_add_permission(self, request):
        return request.user.has_perm("bookshelf.can_create")

    def has_change_permission(self, request, obj=None):
        return request.user.has_perm("bookshelf.can_edit")

    def has_delete_permission(self, request, obj=None):
        return request.user.has_perm("bookshelf.can_delete")

admin.site.register(CustomUser, CustomUserAdmin)
