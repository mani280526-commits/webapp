from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(request):
    return HttpResponse('wer are learning djando')

def show(request):
    obj=HttpResponse('we are good students')
    return obj