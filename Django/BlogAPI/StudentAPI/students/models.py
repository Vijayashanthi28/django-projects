from django.db import models
from .models import Student

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.name
