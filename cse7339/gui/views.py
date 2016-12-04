from django.shortcuts import render
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return render(request, 'index.html', context)
