from django.db import models

# Create your models here.
class Student(models.Model):
    Sno= models.IntegerField()
    Sname= models.CharField(max_length=32)
    Sscore=models.FloatField()
    Saddr=models.CharField(max_length=64)

class Employee(models.Model):
    Eno= models.IntegerField()
    Ename= models.CharField(max_length=32)
    Escore=models.FloatField()
    Eaddr=models.CharField(max_length=64)
