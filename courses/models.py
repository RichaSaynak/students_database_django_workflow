from django.db import models


# Create your models here.
class Course(models.Model):
    course_name = models.TextField(unique=True, blank=False)
    
