from django.shortcuts import render
from my_app.models import Employee
from my_app.models import Student
# Create your views here.
def employee_info(request):
    employ= Employee.objects.order_by('Escore') #Using Database ORM(Object Relational Mapping)
    return render(request, 'test_app/results.html', {'e': employ})

def student_info(request):
    stu= Student.objects.all()
    return render(request, 'test_app/results2.html',{'s':stu})
    #stu= Student.objects.filter(marks_lt=35)
   
