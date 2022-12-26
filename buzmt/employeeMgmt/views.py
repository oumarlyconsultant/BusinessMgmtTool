from django.shortcuts import render
from .models import Employee
from django.http import Http404

# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    return render(request,'employeeMgmt/employee/list.html',{'employees':employees})

def employee_detail(request,id):
    try:
        employee = Employee.objects.get(employeeId=id)
    except Employee.DoesNotExist:
        raise Http404("No employee with this ID found")
    
    return render(request,'employeeMgmt/employee/detail.html',{'employee':employee})
    