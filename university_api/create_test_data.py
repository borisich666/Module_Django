import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_api.settings')
django.setup()

from universities.models import University, Course, UniversityCourse


def create_test_data():
    # Очищаем старые данные (опционально)
    UniversityCourse.objects.all().delete()
    University.objects.all().delete()
    Course.objects.all().delete()

    # Создаем университеты
    uni1 = University.objects.create(name="МГУ", country="Россия")
    uni2 = University.objects.create(name="СПбГУ", country="Россия")
    uni3 = University.objects.create(name="Harvard", country="USA")

    # Создаем курсы
    course1 = Course.objects.create(title="Математика", description="Основы математики")
    course2 = Course.objects.create(title="Физика", description="Основы физики")
    course3 = Course.objects.create(title="Программирование", description="Основы программирования")
    course4 = Course.objects.create(title="История", description="Всемирная история")

    # Создаем связи
    UniversityCourse.objects.create(
        university=uni1,
        course=course1,
        semester="Spring 2025",
        duration_weeks=15
    )
    UniversityCourse.objects.create(
        university=uni1,
        course=course2,
        semester="Spring 2025",
        duration_weeks=12
    )
    UniversityCourse.objects.create(
        university=uni2,
        course=course3,
        semester="Fall 2024",
        duration_weeks=14
    )
    UniversityCourse.objects.create(
        university=uni3,
        course=course4,
        semester="Spring 2025",
        duration_weeks=10
    )

    print("Тестовые данные созданы!")
    print(f"Университеты: {University.objects.count()}")
    print(f"Курсы: {Course.objects.count()}")
    print(f"Связи: {UniversityCourse.objects.count()}")


if __name__ == "__main__":
    create_test_data()