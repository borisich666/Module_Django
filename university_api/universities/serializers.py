from rest_framework import serializers
from .models import University, Course, UniversityCourse


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'country']
        read_only_fields = ['id']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description']
        read_only_fields = ['id']


class UniversityCourseSerializer(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university.name', read_only=True)
    course_title = serializers.CharField(source='course.title', read_only=True)
    course_description = serializers.CharField(source='course.description', read_only=True)

    class Meta:
        model = UniversityCourse
        fields = [
            'id', 'university', 'course', 'university_name', 'course_title',
            'course_description', 'semester', 'duration_weeks'
        ]
        read_only_fields = ['id']


class UniversityCourseListSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    course_description = serializers.CharField(source='course.description', read_only=True)

    class Meta:
        model = UniversityCourse
        fields = ['id', 'course_title', 'course_description', 'semester', 'duration_weeks']
        read_only_fields = ['id']


class CourseStatsSerializer(serializers.Serializer):
    total_courses = serializers.IntegerField()
    average_duration = serializers.FloatField()