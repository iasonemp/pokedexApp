from django.shortcuts import render
from django.http import HttpResponse
import requests 

# Create your views here.

def home(request):
    pokemonList = []
    for i in range(1, 3):
        response=requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json()
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
        pokemonList.append(pokemonDict)
    context = {'pokemonList': pokemonList}
    return render(request, 'components/home.html', context)

def login(request):
    return render(request, 'components/login_register.html')