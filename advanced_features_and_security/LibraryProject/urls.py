from django.contrib import admin
from django.urls import path, include  # include لإضافة روابط التطبيقات

urlpatterns = [
    path("admin/", admin.site.urls),           # لوحة الإدارة
    path("", include("relationship_app.urls")),  # جميع روابط التطبيق الرئيسي
]
