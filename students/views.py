from django.http import JsonResponse
from .models import Student

def student_list(request):
    students = list(Student.objects.values('id', 'name', 'grade', 'major'))
    return JsonResponse(students, safe=False)