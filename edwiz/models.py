from django.db import models
from django.forms import IntegerField

# Create your models here.
class course(models.Model):
    course_name=models.CharField(max_length=30)
    source=models.CharField(max_length=20)
    
class student(models.Model):
    student_name=models.CharField(max_length=20)
   
    enrolled_courses=models.ManyToManyField(course)

    def __str__(self):
        return self.student_name