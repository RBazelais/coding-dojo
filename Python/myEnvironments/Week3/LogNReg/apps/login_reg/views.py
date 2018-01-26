from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from . import models
from . import forms
import random
from forms import RegForm
from models import User
from django.contrib import messages


# Create your views here.
def index(request):
	num = random.randint(3, 11)
	context ={
		'num': num,
		'form': RegForm()
	}
	return render(request, 'index.html', context)


def success(request):
	print "switch paths to success"
	return render(request, 'success.html')

def send_data (request):
	return HttpResponse("send_data is running...")


	