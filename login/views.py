from django.shortcuts import render
from django.contrib.auth import login, authenticate

# Create your views here.

def index(request):
    return render(request, 'index.html')
