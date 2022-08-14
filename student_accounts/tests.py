from django.test import TestCase
from django.urls import reverse
import pytest
from student_accounts.models import Student_Account

# Create your tests here.

# Unit Testing
def test_homepage_access():
    url = reverse('home_account')
    assert url == "/student_accounts/"


# Integration testing without fixtures

# @pytest.mark.django_db
# def test_create_Student_account():
#     student_account = Student_Account.objects.create(
#         username='Pytest',
#         password='test'
#     )
#     assert student_account.username == "Pytest"




# Integration testing with fixtures
@pytest.fixture
def new_student_account(db):
    student_account = Student_Account.objects.create(
           username='Pytest',
           password='test'

    )
    return student_account



def test_search_student_accounts(new_student_account):
    assert Student_Account.objects.filter(username='Pytest').exists()


def test_update_student_account(new_student_account):
    new_student_account.username = 'PytestDj'
    new_student_account.save()
    assert Student_Account.objects.filter(username='PytestDj').exists()




@pytest.fixture
def another_student_account(db):
    student_account = Student_Account.objects.create(
        username='MorePytest'

    )
    return student_account


def test_compare_student_accounts(new_student_account, another_student_account):
    assert new_student_account.pk != another_student_account.pk