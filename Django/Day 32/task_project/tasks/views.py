from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render, redirect

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Frontend view
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})
