from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'components/home.html')

def login(request):
    return render(request, 'components/login_register.html')