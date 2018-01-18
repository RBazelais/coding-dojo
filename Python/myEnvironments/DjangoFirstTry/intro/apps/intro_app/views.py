from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    print "create works"
    return redirect("/")

def show(request, number):
    response = 'placeholder to display blog ' + number
    print "show works"
    return HttpResponse(response)

def edit(request, number):
    response = 'display placeholder to edit blog ' + number
    print "edit works this is blog" + number
    return HttpResponse(response)

def destroy(request, number):
    print "I am actually working"
    return redirect('/')
