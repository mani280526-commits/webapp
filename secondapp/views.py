from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def secondview(request):
    return render(request,'second.html')