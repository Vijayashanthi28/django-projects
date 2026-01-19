from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from .models import Product
from .serializers import ProductSerializer

class ProductFilter(filters.FilterSet):
    price_min = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = filters.CharFilter(field_name='category', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['price_min', 'price_max', 'category']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name']
    filterset_class = ProductFilter


# FRONTEND VIEW
def product_list(request):
    products = Product.objects.all()

    search = request.GET.get('search')
    category = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    order = request.GET.get('order')

    if search:
        products = products.filter(name__icontains=search)

    if category:
        products = products.filter(category__icontains=category)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    if order:
        products = products.order_by(order)

    return render(request, 'products.html', {'products': products})
