from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
# from .models import User

def index(request):
    context = {

    }
    return render(request, 'index.html', context)

def new(request):
    context = {
        
    }
    return render(request, 'new.html', context)

def show(request):
    context = {

    }
    return render(request, 'show.html', context)
# def reset(request):
#     request.session.flush()
#     return redirect('/')