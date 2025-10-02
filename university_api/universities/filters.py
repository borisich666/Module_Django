import django_filters
from django.db import models
from .models import UniversityCourse, University, Course


class UniversityCourseFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='course__title', lookup_expr='icontains')
    semester = django_filters.CharFilter(field_name='semester', lookup_expr='iexact')

    class Meta:
        model = UniversityCourse
        fields = ['title', 'semester']


class UniversityFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter')

    class Meta:
        model = University
        fields = ['search']

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            models.Q(name__icontains=value) |
            models.Q(university_courses__course__title__icontains=value)
        ).distinct()


class CourseFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter')

    class Meta:
        model = Course
        fields = ['search']

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            models.Q(title__icontains=value) |
            models.Q(university_courses__university__name__icontains=value)
        ).distinct()