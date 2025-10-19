from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home / List all posts
    path('', views.PostListView.as_view(), name='home'),

    # User registration and authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # User profile
    path('profile/', views.profile, name='profile'),

    # CRUD for blog posts
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),  # ✅ Required
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
