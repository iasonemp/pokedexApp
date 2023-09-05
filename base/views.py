from django.shortcuts import render
from django.http import HttpResponse
import requests 

# Create your views here.

def home(request):
    response=requests.get('https://pokeapi.co/api/v2/pokemon/').json()
    context = {'response': response}
    return render(request, 'components/home.html', context)

def login(request):
    return render(request, 'components/login_register.html')