from rest_framework.viewsets import ModelViewSet
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
from django.shortcuts import render

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        department_id = self.request.query_params.get('department')
        if department_id:
            return Employee.objects.filter(department_id=department_id)
        return Employee.objects.all()


# -------- FRONTEND VIEWS --------

def departments_page(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments': departments})


def employees_page(request):
    employees = Employee.objects.select_related('department').all()
    return render(request, 'employees.html', {'employees': employees})
