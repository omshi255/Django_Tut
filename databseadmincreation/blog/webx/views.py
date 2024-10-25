from django.shortcuts import render
from . models import chaiVariety
from .models import ChaiReview

from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    chais = chaiVariety.objects.all()
    chaia = ChaiReview.objects.all()
    return render(request,'index.html',{'chais':chais},{'chian':chaia})

def data_val(request,chai_id):
    chai = get_object_or_404(chaiVariety,pk=chai_id)
    return render(request,'data_val.html',{'chai':chai})
