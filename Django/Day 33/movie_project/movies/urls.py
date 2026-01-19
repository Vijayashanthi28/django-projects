from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, movie_list

router = DefaultRouter()
router.register('movies', MovieViewSet)

urlpatterns = [
    path('', movie_list, name='movie_list'),
]

urlpatterns += router.urls
