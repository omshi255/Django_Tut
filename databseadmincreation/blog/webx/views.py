from django.shortcuts import render
from . models import chaiVariety

from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    chais = chaiVariety.objects.all()
    return render(request,'index.html',{'chais':chais})

def data_val(request,chai_id):
    chai = get_object_or_404(chaiVariety,pk=chai_id)
    return render(request,'data_val.html',{'chai':chai})
