from django.shortcuts import render, HttpResponse
from requests import request
from .models import Department, Role, Employee
from datetime import datetime
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')


def allemp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'allemp.html', context)


def addemp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        emp_add = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone,
                           dept_id=dept, role_id=role, hire_date=datetime.now())
        emp_add.save()
        return HttpResponse('Employee added successfully')
    elif request.method == 'GET':
        return render(request, 'addemp.html')
    else:
        pass


def removeemp(request, emp_id=0):
    if emp_id:
        try:
            empidremove = Employee.objects.get(id=emp_id)
            empidremove.delete()
            return render(request, 'removeemp.html')
            # return HttpResponse('Employee Removed')
        except:
            return HttpResponse('Try with Valid ID')
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'removeemp.html', context)


def filteremp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps =emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name=role)

        context = {
            'emps' : emps
        }
        return render(request, 'allemp.html', context)
    elif request.method == 'GET':
        return render(request, 'filteremp.html')
    else:
        return HttpResponse('Something went Wrong!!!')
