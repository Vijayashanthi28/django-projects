from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostFilter(filters.FilterSet):
    author = filters.CharFilter(field_name='author', lookup_expr='icontains')
    created_after = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_before = filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
    tags = filters.CharFilter(field_name='tags', lookup_expr='icontains')

    class Meta:
        model = BlogPost
        fields = ['author', 'created_after', 'created_before', 'tags']


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']
    filterset_class = BlogPostFilter


# FRONTEND VIEW
def blog_list(request):
    posts = BlogPost.objects.all()

    search = request.GET.get('search')
    author = request.GET.get('author')
    tag = request.GET.get('tag')
    order = request.GET.get('order')

    if search:
        posts = posts.filter(title__icontains=search)

    if author:
        posts = posts.filter(author__icontains=author)

    if tag:
        posts = posts.filter(tags__icontains=tag)

    if order:
        posts = posts.order_by(order)

    return render(request, 'blog.html', {'posts': posts})
