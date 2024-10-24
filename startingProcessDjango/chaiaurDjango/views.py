from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello from Home")
    return render(request,'website/index.html')
def about(request):
    return HttpResponse("Hello form About")
def contact(request):
    return HttpResponse("hello from contact")