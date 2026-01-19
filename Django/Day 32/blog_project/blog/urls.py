from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, blog_list

router = DefaultRouter()
router.register('blogposts', BlogPostViewSet)

urlpatterns = [
    path('', blog_list, name='blog_list'),
]

urlpatterns += router.urls
