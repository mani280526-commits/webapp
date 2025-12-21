from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def addition(request):
    if request.method == 'GET':
        return render(request,'calculator/addition.html')
    
    if request.method == 'POST':
        #print(request.POST)
        v1=int(request.POST.get('t1',0))
        v2=int(request.POST.get('t2',0))
        res=v1+v2
        return render(request,'calculator/addition.html',{'result':res})
    
def calculator(request):
    if request.method == 'GET':
        return render(request,'calculator/calculator.html')
    if request.method == 'POST':
        v1= int(request.POST.get('t1',0))
        v2= int(request.POST.get('t2',0))

        if 'add' in request.POST:
            res = v1+v2
            action='Addition'
        elif 'sub' in request.POST:
            res = v2 - v1
            action='Substraction'
        elif 'multi' in request.POST:
            res = v1 * v2
            action='Multiplication'
        else:
            res = v2/v1 
            action='Division'
        return render (request,'calculator/calculator.html',{'result':res,'action':action})
    
def generatetable(request):
    if request.method == 'GET':
        return render(request,'calculator/mtable.html')
    if request.method == 'POST':
        num = int(request.POST.get('t1',0))
        output=[]
        for i in range(1,11):
            output.append(str(num)+' * '+str(i)+' = '+str(i*num))
        return render(request,'mtable.html',{'result':output})

    