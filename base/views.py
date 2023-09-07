from django.shortcuts import render
from django.http import HttpResponse
import requests 

# Create your views here.

def home(request):
    response=requests.get('https://pokeapi.co/api/v2/pokemon/1').json()
    pokemonTypes = []
    for item in response['types']:
        typeName = item['type']['name']
        pokemonTypes.append(typeName)
    pokemonDict = {
    'id': response['id'],
    'sprite': response['sprites']['other']['dream_world']['front_default'],
    'name': response['name'],
    'types': pokemonTypes,
    }
    context = {'pokemonDict': pokemonDict}
    return render(request, 'components/home.html', context)

def login(request):
    return render(request, 'components/login_register.html')