from django.shortcuts import render
from django.views import View
from dbapp.models import Employee
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import EmpSerializer,CustomSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
import json
# create a own api
#class GetEmpAPI(View):
    #def get (self, request):
        #emps = Employee.objects.all()
        #emps = Employee.objects.filter(salary__lt=15000)
        #py_data = [{"empno":emp.empno,"empname":emp.empname,"salary":emp.salary}for emp in emps]
        #json_data = json.dumps(py_data)
        #return JsonResponse(json_data, safe=False)
# Create your views here.
class GetEmpAPI(APIView):
    def get (self, request):
        emps = Employee.objects.all()
        s_obj = EmpSerializer(emps, many=True)
        return Response(s_obj.data)
    def post(self, request):
        s_obj = EmpSerializer(data = request.data)
        if s_obj.is_valid() == True:
            s_obj.save()
            return Response(s_obj.errors,status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
class ModifyEmpAPI(APIView):
    def getemployee(self, pk):
        emp = Employee.objects.get(empno=pk)
        return emp
    def get(self, request, pk):
        emp = self.getemployee(pk)
        s_obj = EmpSerializer(emp)
        return Response(s_obj.data)
    def put(self, request, pk):
        emp = self.getemployee(pk)
        s_obj = EmpSerializer(emp, data=request.data)
        if s_obj.is_valid() == True:
            s_obj.save()
            return Response(status= HTTP_200_OK)
        else:
            return Response(s_obj.errors, status=HTTP_400_BAD_REQUEST)
    def delete(self,request, pk):
        emp = self.getemployee(pk)
        emp.delete()
        return Response(status= HTTP_200_OK)
class CustomInsertAPI(APIView):
    def get(self, request):
        emps=Employee.objects.all()
        s_obj=EmpSerializer(emps, many=True)
        return Response(s_obj.data)
    def post(self, request):
        s_obj = CustomSerializer(data = request.data)
        if s_obj.is_valid() == True:
            s_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)

class CustomModifyAPI(APIView):
    def get(self,request,pk):
        emp = Employee.objects.get(empno=pk)
        s_obj = EmpSerializer(emp)
        return Response(s_obj.data,status=HTTP_200_OK)
    
    def put(self,request,pk):
        emp = Employee.objects.get(empno=pk)
        s_obj = CustomSerializer(emp,data=request.data)
        if s_obj.is_valid() == True:
            s_obj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)             


    



