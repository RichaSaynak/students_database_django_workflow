from django.db import models
from student_accounts.models import Student_Account
from courses.models import Course
from django.db.models import Deferrable, UniqueConstraint

# Create your models here.
class Student(models.Model):
    # student_id = models.BigIntegerField
    student_name = models.TextField(blank=False)
    student_address = models.TextField(blank=False)
    student_email = models.TextField(unique=True, blank=False)
    #student_id = models.ForeignKey(Student_Account, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, through='Grade')
    courses = models.ManyToManyField(Course, through= 'Attendance')
    student_account = models.OneToOneField(Student_Account,on_delete=models.CASCADE)



class Grade (models.Model):
    # class Meta:
    # unique_together = (('student', 'course'))
    # student = models.ForeignKey(Student, on_delete=models.CASCADE, primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # class Meta :
    #     constraints = [
    #         models.UniqueConstraint('student','course', name ='course_student')
    #     ]

       
    # UniqueConstraint(fields=['student','course'], name ='course_student')
        
    # unique_together = (('student', 'course'))
    grade_received = models.CharField(max_length=10, blank=False)



class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_of_attendance = models.DateField(blank=False)
    attended_question = models.CharField(max_length=3, blank=False)

