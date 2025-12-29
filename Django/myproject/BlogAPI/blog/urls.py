from django.urls import path
from .views import (
    BlogPostListCreateView,
    BlogPostDetailView,
    blog_comments
)

urlpatterns = [
    path('blogs/', BlogPostListCreateView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogPostDetailView.as_view(), name='blog-detail'),
    path('blogs/<int:pk>/comments/', blog_comments, name='blog-comments'),
]
