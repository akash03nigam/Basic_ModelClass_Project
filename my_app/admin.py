from django.contrib import admin
from my_app.models import Student
from my_app.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display=['Eno','Ename','Escore']

class StudentAdmin(admin.ModelAdmin):
    list_display=['Sno','Sname','Sscore']
=======
    list_display=['Eno','Ename','Eaddr']

class StudentAdmin(admin.ModelAdmin):
    list_display=['Sno','Sname','Saddr']
>>>>>>> 4bbe4cbf39b97e349e47c85fe0475c091f71a3c6

admin.site.register(Student,StudentAdmin)
admin.site.register(Employee,EmployeeAdmin)
