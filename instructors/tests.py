from django.test import TestCase
from django.urls import reverse
import pytest
from instructors.models import Instructor
from courses.models import Course

# Create your tests here.

# Unit Testing
def test_homepage_access():
    url = reverse('home_instructor')
    assert url == "/instructors/"



# Integration testing without fixtures
# @pytest.mark.django_db
# def test_create_instructor():
#     course_id = Course.objects.create(course_name="Random")
#     instructor = instructor.objects.create(
#         instructor_name='Pytest',
#         instructor_short_id='test',
#         course = course_id

#     )
#     assert instructor.instructor_name == "Pytest"



# Integration testing with fixtures
@pytest.fixture
def new_instructor(db):
    course_id = Course.objects.create(course_name="Random")
    instructor = Instructor.objects.create(
        instructor_name='Pytest',
        instructor_short_id='test',
        course = course_id

    )
    return instructor



def test_search_instructors(new_instructor):
    assert Instructor.objects.filter(instructor_name='Pytest').exists()

def test_update_instructor(new_instructor):
    new_instructor.instructor_name = 'Pytest-Django'
    new_instructor.save()
    assert Instructor.objects.filter(instructor_name='Pytest-Django').exists()




@pytest.fixture
def another_instructor(db):
    course_id = Course.objects.create(course_name="Maths")
    instructor = Instructor.objects.create(
        instructor_name='More-Pytest',
        instructor_short_id ='testi',
        course = course_id

    )
    return instructor


def test_compare_instructors(new_instructor, another_instructor):
    assert new_instructor.pk != another_instructor.pk
