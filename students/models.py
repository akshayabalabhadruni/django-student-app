
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=20)
    major = models.CharField(max_length=50)

    def __str__(self):
        return self.name