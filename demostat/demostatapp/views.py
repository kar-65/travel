from django.shortcuts import render
from django.http import HttpResponse
from . models import places
from . models import team
# Create your views here.

def demofun(request):
    #return HttpResponse("hi hellow")
    obj=places.objects.all()
    tm= team.objects.all()
    return render(request,'index.html',{'result': obj,'team': tm})