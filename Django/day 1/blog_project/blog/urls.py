# blog/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    
    # Test page
    path('test/', views.test_view, name='test'),
    
    # Blog posts
    path('posts/', views.post_list, name='post-list'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    
    # API endpoints (if you have API views)
    path('api/', include('blog.api_urls')),  # If you have separate API URLs
]