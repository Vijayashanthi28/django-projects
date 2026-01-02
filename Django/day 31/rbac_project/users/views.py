from django.shortcuts import render, redirect
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdminOrReadOnly

# API View
class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

# Frontend Views
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST['name'],
            price=request.POST['price']
        )
        return redirect('/')
