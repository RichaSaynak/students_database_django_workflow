from django.db import models
from courses.models import Course

# Create your models here.
class Instructor(models.Model):
    instructor_name = models.TextField(blank=False)
    instructor_short_id = models.CharField(max_length=5, unique=True, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)