from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def result(request):
    return render(request, "result.html")

def process(request):
    context = {
        'name': request.POST['name'],
        'dojo_location' : request.POST['dojo_location'],
        'programming_language' : request.POST['programming_language'],
        'comment' : request.POST['comment']
    }
    # get post of this key/object/val
    return render(request, 'result.html', context)

def go_back(request):
    return redirect('/')