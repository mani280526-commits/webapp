from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee,Department
from django.contrib import messages
# Create your views here.

def dbprocessing(request):
    return HttpResponse('DB processing request is triggred')

def insertemployee(request):
    if request.method == 'GET':
        depts = Department.objects.all()
        return render(request,'dbapp/insert.html',{'departments':depts})
    if request.method == 'POST':
        eno = int(request.POST['eno'])
        ename = request.POST['ename']
        esal = int(request.POST['esal'])
        dno = int(request.POST['dept'])
        dobj = Department.objects.get(deptno=dno)
        epic = request.FILES['epic']
        evideo = request.FILES['evideo']

        eobj=Employee.objects.create(empno=eno,empname=ename,salary=esal,dept=dobj,profile_pic=epic,video = evideo)

        #messages.success(request,'Data inserted successfully')
        return redirect('selecturl')
    
def selectemployee(request):
    if request.method == 'GET':
        emps = Employee.objects.all()
        return render(request,'dbapp/select.html',{'employees':emps})
def updateemployee(request,eno):
    eobj = Employee.objects.get(empno=eno)
    depts = Department.objects.all()
    if request.method == 'GET':
        #select * from employee where empno=eno
        return render(request,'dbapp/update.html',{'employee':eobj,'departments': depts})
    if request.method == 'POST':
        eobj.empname = request.POST.get('ename','')
        eobj.salary = request.POST.get('esal',0)
        dno = request.POST.get('dept')
    if dno :
        eobj.dept = Department.objects.get(deptno=dno)
    if 'epic' in request.FILES:
        eobj.profile_pic = request.FILES['epic']
    if 'evideo' in request.FILES:
        eobj.video = request.FILES['evideo']
        #empobj=Employee(empno=eno,empname=ename,salary=esal)
        eobj.save()
        #messages.success(request,'Updated successfully')
        return redirect('selecturl')
def deleteemployee(request,eno):
    if request.method == 'GET':
        emp = Employee.objects.get(empno=eno)
        return render(request,'dbapp/delect.html',{'employee':emp})
    if request.method == 'POST':
        emp = Employee.objects.get(empno=eno)
        emp.delete()
        return redirect('selecturl')