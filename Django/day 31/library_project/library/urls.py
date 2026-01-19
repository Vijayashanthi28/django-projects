from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AuthorViewSet, BookViewSet
from . import views

router = SimpleRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet, basename='book')

urlpatterns = [
    path('api/', include(router.urls)),
    path('authors/', views.authors_page),
    path('books/', views.books_page),
]
