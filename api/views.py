from django.shortcuts import render
from django.views import View
from dbapp.models import Employee
from django.http import JsonResponse
import json
# Create your views here.
class GetEmpAPI(View):
    def get (self, request):
        #emps = Employee.objects.all()
        emps = Employee.objects.filter(salary__lt=15000)
        py_data = [{"empno":emp.empno,"empname":emp.empname,"salary":emp.salary}for emp in emps]
        json_data = json.dumps(py_data)
        return JsonResponse(json_data, safe=False)

