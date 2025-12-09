from django.shortcuts import render
from .models import Course, Concept

def course_list(request):
    courses = Course.objects.select_related('concept').all()
    concepts = Concept.objects.all()
    return render(request, "index.html", {"courses": courses, "concepts": concepts})
