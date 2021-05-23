from django.db import models

# Create your models here.
class Student(models.Model):
    Sno= models.IntegerField()
    Sname= models.CharField(max_length=32)
    Sscore=models.FloatField()
    
 
    def __str__(self):
        return self.Sname
    
class Employee(models.Model):
    Eno= models.IntegerField()
    Ename= models.CharField(max_length=32)
    Escore=models.FloatField()
    

    def __str__(self):
        return self.Ename
    
