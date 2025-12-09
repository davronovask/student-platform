from django.contrib import admin
from django.urls import path
from core.views import course_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', course_list, name='index'),
]
