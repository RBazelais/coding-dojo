from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from models import *
import random

from forms import RegForm
from django.contrib import messages

# Create your views here.
def new(request):
	num = random.randint(3, 11)
	context ={
		'num': num,
		'form': RegForm()
	}
	return render(request, 'houses/new.html', context)

def create(request):
	errors = Student.objects.basic_validator(request.POST)
	student = Student(name=peep)
	student = Student.objects.all()[random.randint(0,3)]
	student.cult = House.objects.first()
	student.course = Course.objects.first()
	student.save() #whyyyy whaaaa
	# is it valid?
	def is_valid(RegForm):
		# Yes
		if len(errors) == 0:
			print "Form was valid!"
			request.session['peep'] = 'peep'
			# create student
			# Login
			# redirect to index
			return render(request, "houses/index.html")
		# No
		else:
			for error in errors:
				# display errors
				messages.error(request, errors[error])
			# redirect to new
			return redirect("/")
	
		

def index(request):
	context = {
		# What students belong to these houses
		'thunderbird' : Student.objects.filter(cult__name='Thunder Bird'),
		'wampii' : Student.objects.filter(cult__name='Wampus'),

		# What houses have these students associated with them
		'puks' : House.objects.get(name='Horned Serpent').peeps.all(),
		'snakes' : House.objects.get(name='Pukwudgie').peeps.all()
	}
	return render(request, 'houses/index.html', context)

def show(request, info):
	print info
	return

	#peep = request.POST['name']
	# student = Student(name=peep)
	# student = Student.objects.all()[random.randint(0,3)]
	# student.cult = House.objects.first()
	# student.course = Course.objects.first()
	# student.save() #whyyyy whaaaa
	#request.session['peep'] = peep
