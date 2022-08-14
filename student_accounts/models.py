from django.db import models
from django.contrib.auth.hashers import make_password




# Create your models here.
class Student_Account(models.Model):
    username = models.CharField(max_length=10, unique=True, blank=False)
    # password = models.CharField(max_length=8, blank=False)
    password = models.TextField(blank=False)
    # password = make_password(models.TextField(max_length=8, blank=False))
    # password = scramble((models.TextField(max_length=8, blank=False)))
    
    

