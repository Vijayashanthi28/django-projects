from django.urls import path, include
from .views import post_list, post_detail, post_create
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet

router = DefaultRouter()
router.register('posts', BlogPostViewSet)

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('create/', post_create, name='post_create'),
    path('api/', include(router.urls)),
]
