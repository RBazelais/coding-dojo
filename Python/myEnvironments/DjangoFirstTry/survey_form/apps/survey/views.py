from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Hello, I am your first request!"
    html = "survey_templates/index.html"
    test = "akshbvkyaeru"
    
    return render(request, html)

def result(request):
    return HttpResponse(response)

def process(request):
    
    print(request.POST[{name}]) # get post of this key/object/val
    return redirect("/result")