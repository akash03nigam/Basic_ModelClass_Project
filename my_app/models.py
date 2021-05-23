from django.db import models

# Create your models here.
class Student(models.Model):
    Sno= models.IntegerField()
    Sname= models.CharField(max_length=32)
    Saddr=models.CharField(max_length=64)
 
    def __str__(self):
        return self.Sname
    
class Employee(models.Model):
    Eno= models.IntegerField()
    Ename= models.CharField(max_length=32)
    Eaddr=models.CharField(max_length=64)

    def __str__(self):
        return self.Ename
    
