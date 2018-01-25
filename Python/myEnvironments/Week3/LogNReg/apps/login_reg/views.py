from __future__ import unicode_literals
from django.shortcuts import render, redirect
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
	return render(request, 'success.html')

def send_data (request):
	form = RegForm(request.POST)
	form.save()
	print "Data has been sent"

	errors = User.objects.basic_validator(request.POST)
	User.save()

	def is_valid(RegForm):
		# Yes
		if len(errors) == 0:
			print "Form was valid!"
			request.session['current_user'] = 'current_user'
			return redirect("/success.html")
		# No
		else:
			for error in errors:
				# display errors
				messages.error(request, errors[error])
			# redirect to new
			return redirect("/")

	