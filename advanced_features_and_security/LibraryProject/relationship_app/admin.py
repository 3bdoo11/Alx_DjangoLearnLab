from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("profile_picture",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("profile_picture",)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
