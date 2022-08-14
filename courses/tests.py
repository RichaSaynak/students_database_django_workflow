from django.test import TestCase
from django.urls import reverse
import pytest
from courses.models import Course

# Create your tests here.

# Unit Testing
def test_homepage_access():
    url = reverse('home_course')
    assert url == "/courses/"



# Integration testing without fixtures
# @pytest.mark.django_db
# def test_create_course():
#     course = Course.objects.create(
#         course_name='Pytest'

#     )
#     assert course.course_name == "Pytest"


# Integration testing with fixtures
@pytest.fixture
def new_course(db):
    course = Course.objects.create(
        course_name='Pytest'

    )
    return course



def test_search_courses(new_course):
    assert Course.objects.filter(course_name='Pytest').exists()

def test_update_course(new_course):
    new_course.course_name = 'Pytest-Django'
    new_course.save()
    assert Course.objects.filter(course_name='Pytest-Django').exists()




@pytest.fixture
def another_course(db):
    course = Course.objects.create(
        course_name='More-Pytest'

    )
    return course


def test_compare_courses(new_course, another_course):
    assert new_course.pk != another_course.pk