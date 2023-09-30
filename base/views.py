from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pokemon
import requests

def detail(request, pokemon_name):
    pokemon = Pokemon.objects.get(name=pokemon_name)
    context = {'starter_form': pokemon.starter_form, 
               'tier_1_evolution' : pokemon.tier_1_evolution, 
               'tier_2_evolution' : pokemon.tier_2_evolution,
               'height' : pokemon.height,
               'weight' : pokemon.weight,
               'hp' : pokemon.hp,
               'attack' : pokemon.attack,
               'defense' : pokemon.defense,
               'speed' : pokemon.speed,
               'special_attack' : pokemon.special_attack,
               'special_defense' : pokemon.special_defense,}
    return JsonResponse(context)

# Create your views here.
def populatePokemonDatabase(request):
    for i in range(10,11):
        response=requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json()
                ########## EVOLUTIONS ##########
        species_link = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{i}').json()
        evolution_link = species_link['evolution_chain']['url']
        evolution_chain=requests.get(evolution_link).json()

        ## STARTER
        starter_form = evolution_chain['chain']['species']['name']

        ## FIRST EVOLUTION
        first_evo = evolution_chain['chain']['evolves_to']
        if first_evo:
            ## IN CASE OF MULTIPLE EVOLUTIONS
            tier_1_evolution = []
            for evo in range(len(first_evo)):
                tier_1_evolution.append(first_evo[evo]['species']['name'])
            tier_1_evolution = ':'.join(tier_1_evolution)
        
        
        ## SECOND EVOLUTION
            second_evo = first_evo[0]['evolves_to']
            if second_evo:
                tier_2_evolution = []
                for evo in range(len(second_evo)):
                    tier_2_evolution.append(second_evo[evo]['species']['name'])
                tier_2_evolution = ':'.join(tier_2_evolution)
                
        ########## TYPES ##########
        types = []
        for item in response['types']:
            typeName = item['type']['name']
            types.append(typeName)
        types = ':'.join(types)

        response['name'] = Pokemon.objects.create(
            name = response['name'],
            starter_form = starter_form,
            tier_1_evolution = tier_1_evolution,
            tier_2_evolution = tier_2_evolution,
            types = types,
            pokedex_number = response['id'],
            sprite = response['sprites']['other']['dream_world']['front_default'],
            height = response['height'], # dm, /10 = m
            weight = response['weight'], # dag, /10 = kg
            hp = response['stats'][0]['base_stat'],
            attack = response['stats'][1]['base_stat'],
            defense = response['stats'][2]['base_stat'],
            special_attack = response['stats'][3]['base_stat'],
            special_defense = response['stats'][4]['base_stat'],
            speed = response['stats'][5]['base_stat'],
        )
    context = {}
    return render(request, 'components/populate.html', context)

def home(request):
    pokemons = Pokemon.objects.all()
    context = {'pokemons': pokemons}
    return render(request, 'components/home.html', context)

def login(request):
    return render(request, 'components/login_register.html')