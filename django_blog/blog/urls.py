from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Post CRUD URLs
    path('post/new/', views.post_create, name='post-create'),
    path('post/<int:pk>/edit/', views.post_update, name='post-update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post-delete'),
]
