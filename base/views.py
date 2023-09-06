from django.shortcuts import render
from django.http import HttpResponse
import requests 

# Create your views here.

def home(request):
    response=requests.get('https://pokeapi.co/api/v2/pokemon/1').json()
    pokemonDict = {}
    pokemonDict['id'] = response['id']
    pokemonDict['name'] = response['name']
    pokemonTypes = []
    for item in response['types']:
        typeName = item['type']['name']
        pokemonTypes.append(typeName)
    pokemonDict['types'] = pokemonTypes
    context = {'pokemonName': pokemonDict['name'], 'pokemonTypes': pokemonDict['types']}
    return render(request, 'components/home.html', context)

def login(request):
    return render(request, 'components/login_register.html')