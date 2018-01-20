from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from random import randint
from models import *

# Create your views here.
def index(request):
    context = { # passes values between server and template engine
        "red" : House.objects.get(id=1).students.all(),
        "blue" : House.objects.get(id=2).students.all(),
        "green" : House.objects.get(id=3).students.all(),
        "purple" : House.objects.get(id=4).students.all()
    }
    return render(request, 'index.html', context)

def sort(request):
    if  request.method == "POST":
        name = request.POST['name']

        house_id = randint(1,4)
        current_house = House.objects.get(id=house_id)
        
        current_house.students.create(name=name)
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')
