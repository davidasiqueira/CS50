from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello_world/index.html')

def great(request, name):
    return render(request, 'hello_world/great.html', {
        "name": name.capitalize()
    })

