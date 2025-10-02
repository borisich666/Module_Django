from django.contrib import admin
from .models import University, Course, UniversityCourse


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    search_fields = ['name', 'country']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'description']


@admin.register(UniversityCourse)
class UniversityCourseAdmin(admin.ModelAdmin):
    list_display = ['university', 'course', 'semester', 'duration_weeks']
    list_filter = ['semester', 'university']
    search_fields = ['university__name', 'course__title', 'semester']