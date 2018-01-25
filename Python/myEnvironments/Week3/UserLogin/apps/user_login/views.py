from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *

# Create your views here.
def index(request):
    response = "It's working! ITS ALIVE!!!"
    return HttpResponse(response)
