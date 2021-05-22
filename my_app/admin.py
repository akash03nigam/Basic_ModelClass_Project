from django.contrib import admin
from my_app.models import Student
from my_app.models import Employee
# Register your models here.
admin.site.register(Student)
admin.site.register(Employee)