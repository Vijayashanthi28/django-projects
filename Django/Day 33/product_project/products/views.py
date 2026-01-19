from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Product
from .serializers import ProductSerializer


# API VIEW
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'category']
    ordering_fields = ['price', 'name']


# FRONTEND VIEW
def product_list(request):
    products = Product.objects.all()

    search = request.GET.get('search')
    order = request.GET.get('order')

    if search:
        products = products.filter(name__icontains=search) | products.filter(category__icontains=search)

    if order:
        products = products.order_by(order)

    return render(request, 'products.html', {'products': products})
