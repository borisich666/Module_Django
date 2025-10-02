from django.db import models


class University(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Universities"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.country})"


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class UniversityCourse(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='university_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='university_courses')
    semester = models.CharField(max_length=50)
    duration_weeks = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['university', 'course', 'semester'],
                name='unique_course_per_semester'
            )
        ]
        ordering = ['semester', 'course__title']

    def __str__(self):
        return f"{self.course.title} at {self.university.name} ({self.semester})"