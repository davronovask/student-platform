from django.contrib import admin
from .models import Course, Concept

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'description', 'get_color', 'get_icon', 'is_active')
    list_filter = ('is_active', 'concept')

    def get_color(self, obj):
        return obj.concept.color
    get_color.short_description = 'Цвет'

    def get_icon(self, obj):
        return obj.concept.icon
    get_icon.short_description = 'Иконка'


@admin.register(Concept)
class ConceptAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon', 'color')
