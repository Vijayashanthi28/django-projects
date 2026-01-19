from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet
from . import views

router = DefaultRouter()
router.register('departments', DepartmentViewSet)
router.register('employees', EmployeeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('departments/', views.departments_page),
    path('employees/', views.employees_page),
]
