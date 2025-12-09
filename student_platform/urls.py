from django.contrib import admin
from django.urls import path
from core.views import courses_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', courses_list, name='index'),
]
