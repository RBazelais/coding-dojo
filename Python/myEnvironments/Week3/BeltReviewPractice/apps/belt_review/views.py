from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from models import *
from forms import *

# Create your views here.
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST or None)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            NewUser.objects.create(
                request.POST['name'],
                request.POST['alias']
                
            )
            email = form.cleaned_data.get('email'),
            password = form.cleaned_data.get('password'),
            confirm_password = form.cleaned_data.get('confirm_password')

            #print results
            # print name
            # print last_name
            # print email
            # print password
            # redirect to a new URL:
            return HttpResponseRedirect('/success')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'belt_review/index.html', {'form': form})

def process(request):
    return HttpResponse('a thing')


def success(request):
	print "switch paths to success"
	return render(request, 'belt_review/success.html')