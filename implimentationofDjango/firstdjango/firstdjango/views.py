from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse ("Hello from Home")
    return render (request,'index.html')

def about(request):
    return HttpResponse  ("Hello from about")

def contact(request):
    return HttpResponse  ("Hello from contact")

def services(request):
    return HttpResponse ("Hello from services")

def info(request):
    return HttpResponse ("Hello from info")


