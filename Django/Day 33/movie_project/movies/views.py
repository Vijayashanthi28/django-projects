from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from .models import Movie
from .serializers import MovieSerializer


# CUSTOM FILTERS
class MovieFilter(filters.FilterSet):
    genre = filters.CharFilter(field_name='genre', lookup_expr='icontains')
    release_after = filters.DateFilter(field_name='release_date', lookup_expr='gte')
    release_before = filters.DateFilter(field_name='release_date', lookup_expr='lte')
    rating_min = filters.NumberFilter(field_name='rating', lookup_expr='gte')
    rating_max = filters.NumberFilter(field_name='rating', lookup_expr='lte')

    class Meta:
        model = Movie
        fields = ['genre', 'release_after', 'release_before', 'rating_min', 'rating_max']


# API VIEW
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('-rating', 'release_date')
    serializer_class = MovieSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MovieFilter

    ordering_fields = ['release_date', 'rating']
    ordering = ['-rating', 'release_date']  # default sorting


# FRONTEND VIEW
def movie_list(request):
    movies = Movie.objects.all().order_by('-rating', 'release_date')

    genre = request.GET.get('genre')
    min_rating = request.GET.get('min_rating')
    max_rating = request.GET.get('max_rating')
    order = request.GET.get('order')

    if genre:
        movies = movies.filter(genre__icontains=genre)

    if min_rating:
        movies = movies.filter(rating__gte=min_rating)

    if max_rating:
        movies = movies.filter(rating__lte=max_rating)

    if order:
        movies = movies.order_by(order)

    return render(request, 'movies.html', {'movies': movies})
