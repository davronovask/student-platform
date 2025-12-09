from django.shortcuts import render
from .models import Course, Concept

def courses_list(request):
    courses = Course.objects.select_related('concept').all()
    return render(request, 'index.html', {'courses': courses})
