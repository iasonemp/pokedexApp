from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def home(request):
    pokemonList = []
    for i in range(1, 9, 3):
        response=requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json()

        ## EVOLUTIONS
        pokemonEvolutions = []
        species_link = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{i}').json()
        evolution_link = species_link['evolution_chain']['url']
        evolution_chain=requests.get(evolution_link).json()
        starter = evolution_chain['chain']['species']['name']
        pokemonEvolutions.append(starter)
        t1evo = evolution_chain['chain']['evolves_to']
        if t1evo:
            t1EvoList = []
            for evo in range(len(t1evo)):
                t1EvoList.append(t1evo[evo]['species']['name'])
            print(t1EvoList)
            pokemonEvolutions.append(t1EvoList)
            t2evo = t1evo[0]['evolves_to']
            if t2evo:
                t2EvoList = []
                for evo in range(len(t2evo)):
                    t2EvoList.append(t2evo[evo]['species']['name'])
                pokemonEvolutions.append(t2EvoList)

        ## TYPES
        pokemonTypes = []
        for item in response['types']:
            typeName = item['type']['name']
            pokemonTypes.append(typeName)

        pokemonDict = {
        'id': response['id'],
        'sprite': response['sprites']['other']['dream_world']['front_default'],
        'name': response['name'],
        'types': pokemonTypes,
        'evolutions': pokemonEvolutions,
        }

        pokemonList.append(pokemonDict)
    context = {'pokemonList': pokemonList}
    return render(request, 'components/home.html', context)

def login(request):
    return render(request, 'components/login_register.html')