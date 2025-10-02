from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django.db.models import Count, Avg

from .models import University, Course, UniversityCourse
from .serializers import (
    UniversitySerializer, CourseSerializer, UniversityCourseSerializer,
    UniversityCourseListSerializer, CourseStatsSerializer
)
from .filters import UniversityCourseFilter, UniversityFilter, CourseFilter


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = UniversityFilter
    search_fields = ['name', 'country']

    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        """Показать все курсы университета с фильтрацией и сортировкой"""
        university = self.get_object()
        university_courses = UniversityCourse.objects.filter(university=university)

        # Применяем фильтрацию
        filterset = UniversityCourseFilter(request.GET, queryset=university_courses)
        filtered_queryset = filterset.qs

        # Применяем сортировку
        ordering = request.GET.get('ordering', 'duration_weeks')
        if ordering.lstrip('-') in ['duration_weeks', 'semester', 'course__title']:
            filtered_queryset = filtered_queryset.order_by(ordering)

        page = self.paginate_queryset(filtered_queryset)
        if page is not None:
            serializer = UniversityCourseListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = UniversityCourseListSerializer(filtered_queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def course_stats(self, request, pk=None):
        """Статистика курсов университета"""
        university = self.get_object()
        stats = university.university_courses.aggregate(
            total_courses=Count('id'),
            average_duration=Avg('duration_weeks')
        )

        # Округляем среднюю длительность
        if stats['average_duration']:
            stats['average_duration'] = round(stats['average_duration'], 1)
        else:
            stats['average_duration'] = 0.0

        serializer = CourseStatsSerializer(stats)
        return Response(serializer.data)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = CourseFilter
    search_fields = ['title', 'description']


class UniversityCourseViewSet(viewsets.ModelViewSet):
    queryset = UniversityCourse.objects.all()
    serializer_class = UniversityCourseSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = UniversityCourseFilter
    ordering_fields = ['duration_weeks', 'semester']
    ordering = ['duration_weeks']