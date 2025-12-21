from django.shortcuts import render
from django.views import View
# Create your views here.

class Calculator(View):
    def get(self,request):
        return render(request,'classapp/addition.html')
    def post(self,request):
        v1 = int(request.POST['t1'])
        v2 = int(request.POST['t2'])
        res = v1+v2
        return render(request,'classapp/addition.html',{'result':res})
class Calculator2(Calculator):
    pass