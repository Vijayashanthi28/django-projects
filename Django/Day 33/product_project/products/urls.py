from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, product_list

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', product_list, name='product_list'),
]

urlpatterns += router.urls
