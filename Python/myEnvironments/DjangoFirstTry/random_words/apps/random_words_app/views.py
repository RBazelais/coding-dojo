from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# the index function is called when root is visited
def index(request):
    visit_count = request.session.get('visit count is ', 0)
    request.session['visit_count'] = visit_count + 1
    html = "random_words_app_templates/index.html"
    test = "akshbvkyaeru"
    data = {
        "word" : get_random_string(length=12)
    }
    return render(request, html, data)
