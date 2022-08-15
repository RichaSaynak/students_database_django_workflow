from django.test import TestCase
from django.urls import reverse
import pytest

from students.models import Student, Grade, Attendance
from student_accounts.models import Student_Account
from courses.models import Course

# Create your tests here.


# Unit Testing
def test_homepage_access():
    url = reverse('home_student')
    assert url == "/"




# Integration Testing without fixture
# @pytest.mark.django_db
# def test_create_student():
#     account_id = Student_Account.objects.create(username= "py", password= "123")
#     student = Student.objects.create(
#         student_name='Pytest',
#         student_address='test',
#         student_email ='test@gmail.com',
#         student_account = account_id
        
#     )
#     assert student.student_name == "Pytest"



 # Integration Testing using fixtures
 # 
 
@pytest.fixture
def new_student(db):
    account_id = Student_Account.objects.create(username= "py", password= "123")
    student = Student.objects.create(
        student_name='Pytest',
        student_address='test',
        student_email ='test@gmail.com',
        student_account = account_id
        
    )
    return student



def test_search_students(new_student):
    assert Student.objects.filter(student_name='Pytest').exists()

def test_update_student(new_student):
    new_student.student_name = 'Pytest-Django'
    new_student.save()
    assert Student.objects.filter(student_name='Pytest-Django').exists()




@pytest.fixture
def another_student(db):
    account_id = Student_Account.objects.create(username= "pymore", password= "1234")
    student = Student.objects.create(
        student_name='MorePytest',
        student_address='moretest',
        student_email ='moretest@gmail.com',
        student_account = account_id
    )
    return student


def test_compare_students(new_student, another_student):
    assert new_student.pk != another_student.pk




# ------FOR GRADES TABLE -----------------------------


# Integration testing without fixtures
# @pytest.mark.django_db
# def test_create_grade():
#     account_id = Student_Account.objects.create(username= "py", password= "123")
#     student_id = Student.objects.create(student_name ="Mike", student_address= 'Montreal', student_email = 'ms@gmail.com', student_account=account_id)
#     course_id = Course.objects.create(course_name='Maths')
#     grade = Grade.objects.create(
#         student = student_id,
#         course =course_id,
#         grade_received ='A',
        
        
#     )
#     assert grade.grade_received == "A"




# Integration testing with fixtures

@pytest.fixture
def new_grade(db):
    account_id = Student_Account.objects.create(username= "py", password= "123")
    student_id = Student.objects.create(student_name ="Mike", student_address= 'Montreal', student_email = 'ms@gmail.com', student_account=account_id)
    course_id = Course.objects.create(course_name='Maths')
    grade = Grade.objects.create(
        student = student_id,
        course =course_id,
        grade_received ='A',
                
    )
    return grade



def test_search_grades(new_grade):
    assert Grade.objects.filter(grade_received='A').exists()

def test_update_grade(new_grade):
    new_grade.grade_received = 'A plus'
    new_grade.save()
    assert Grade.objects.filter(grade_received='A plus').exists()


@pytest.fixture
def another_grade(db):
    account_id = Student_Account.objects.create(username= "pymore", password= "1234")
    student_id = Student.objects.create(student_name ="Dave", student_address= 'Toronto', student_email = 'ds@gmail.com', student_account=account_id)
    course_id = Course.objects.create(course_name='Science')
    grade = Grade.objects.create(
        student = student_id,
        course =course_id,
        grade_received ='B',
                
    )
    return grade



def test_compare_grades(new_grade, another_grade):
    assert new_grade.pk != another_grade.pk





# -------------------------FOR ATTENDANCES --------------------------------------------------------------

# Integration testing without fixtures
# @pytest.mark.django_db
# def test_create_attendance():
#     account_id = Student_Account.objects.create(username= "py", password= "123")
#     student_id = Student.objects.create(student_name ="Mike", student_address= 'Montreal', student_email = 'ms@gmail.com', student_account=account_id)
#     course_id = Course.objects.create(course_name='Maths')
#     attend = Attendance.objects.create(
#         student = student_id,
#         course =course_id,
#         date_of_attendance ='2022-01-09',
#         attended_question = 'Yes'
        
        
#     )
#     assert attend.date_of_attendance == "2022-01-09"
#     assert attend.attended_question == 'Yes'


# Integration testing with fixtures
@pytest.fixture
def new_attendance(db):
    account_id = Student_Account.objects.create(username= "py", password= "123")
    student_id = Student.objects.create(student_name ="Mike", student_address= 'Montreal', student_email = 'ms@gmail.com', student_account=account_id)
    course_id = Course.objects.create(course_name='Maths')
    attend = Attendance.objects.create(
        student = student_id,
        course =course_id,
        date_of_attendance ='2022-01-09',
        attended_question = 'Yes'
        
     )
    return attend 


def test_search_attendances(new_attendance):
    assert Attendance.objects.filter(date_of_attendance='2022-01-09', attended_question='Yes').exists()

def test_update_attendance(new_attendance):
    new_attendance.date_of_attendance = '2022-01-20'
    new_attendance.attended_question = 'No'
    new_attendance.save()
    assert Attendance.objects.filter(date_of_attendance='2022-01-20', attended_question='No').exists()



@pytest.fixture
def another_attendance(db):
    account_id = Student_Account.objects.create(username= "pymored", password= "1234")
    student_id = Student.objects.create(student_name ="Dave", student_address= 'Toronto', student_email = 'dss@gmail.com', student_account=account_id)
    course_id = Course.objects.create(course_name='Science')
    attend = Attendance.objects.create(
        student = student_id,
        course =course_id,
        date_of_attendance ='2022-01-22',
        attended_question = 'No'
        
     )
    return attend


def test_compare_attendances(new_attendance, another_attendance):
    assert new_attendance.pk != another_attendance.pk


