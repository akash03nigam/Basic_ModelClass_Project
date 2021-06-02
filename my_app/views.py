from django.shortcuts import render
from my_app.models import Employee
from my_app.models import Student
# Create your views here.
def employee_info(request):
    employ= Employee.objects.all()
    return render(request, 'test_app/results.html', {'e': employ})

def student_info(request):
    stu= Student.objects.order_by('Sscore')
    return render(request, 'test_app/results2.html',{'s':stu})