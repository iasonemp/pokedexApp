from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def populatePokemonModel(request):
    context = {}
    return render(request, 'components/populate.html', context)

def home(request):
    # each index has the info of 1 pokemon
    pokemonList = []
    # bulbasaur, charmander, squirtle
    for i in range(1, 4):
        response=requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json()

        ########## EVOLUTIONS ##########
        pokemonEvolutions = []
        species_link = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{i}').json()
        evolution_link = species_link['evolution_chain']['url']
        evolution_chain=requests.get(evolution_link).json()

        ## STARTER
        tier1 = evolution_chain['chain']['species']['name']
        pokemonEvolutions.append(tier1)

        ## FIRST EVOLUTION
        first_evo = evolution_chain['chain']['evolves_to']
        if first_evo:
            ## IN CASE OF MULTIPLE EVOLUTIONS
            tier2 = []
            for evo in range(len(first_evo)):
                tier2.append(first_evo[evo]['species']['name'])
            tier2 = ':'.join(tier2)
            pokemonEvolutions.append(tier2)
            
        ## SECOND EVOLUTION
            second_evo = first_evo[0]['evolves_to']
            if second_evo:
                tier3 = []
                for evo in range(len(second_evo)):
                    tier3.append(second_evo[evo]['species']['name'])
                tier3 = ':'.join(tier3)
                pokemonEvolutions.append(tier3)
                

        ########## TYPES ##########
        pokemonTypes = []
        for item in response['types']:
            typeName = item['type']['name']
            pokemonTypes.append(typeName)

        ########## STATS ##########
        statList = []
        for i in range(6):
            stat = {response['stats'][i]['stat']['name'] : response['stats'][i]['base_stat']}
            statList.append(stat)
                
        pokemonDict = {
        'name': response['name'],
        'id': response['id'],
        'sprite': response['sprites']['other']['dream_world']['front_default'],
        'height' : response['height'],
        'weight' : response['weight'],
        'evolutions': pokemonEvolutions,
        'types': pokemonTypes,
        'stats': statList,
        }

        pokemonList.append(pokemonDict)
    context = {'pokemonList': pokemonList}
    return render(request, 'components/home.html', context)

def login(request):
    return render(request, 'components/login_register.html')