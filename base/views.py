from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon
import requests

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

# def populatePokemonDatabase(request):
#     for i in range(1, 4):
#         response=requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json()
        # ########## EVOLUTIONS ##########
        # pokemonEvolutions = []
        # species_link = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{i}').json()
        # evolution_link = species_link['evolution_chain']['url']
        # evolution_chain=requests.get(evolution_link).json()

        # ## STARTER
        # tier1 = evolution_chain['chain']['species']['name']
        # pokemonEvolutions.append(tier1)

#         ## FIRST EVOLUTION
#         first_evo = evolution_chain['chain']['evolves_to']
#         if first_evo:
#             ## IN CASE OF MULTIPLE EVOLUTIONS
#             tier2 = []
#             for evo in range(len(first_evo)):
#                 tier2.append(first_evo[evo]['species']['name'])
#             tier2 = ':'.join(tier2)
#             pokemonEvolutions.append(tier2)
            
        # ## SECOND EVOLUTION
        #     second_evo = first_evo[0]['evolves_to']
        #     if second_evo:
        #         tier3 = []
        #         for evo in range(len(second_evo)):
        #             tier3.append(second_evo[evo]['species']['name'])
        #         tier3 = ':'.join(tier3)
#                 pokemonEvolutions.append(tier3)

    # context = {}
    # return render(request, 'components/populate.html', context)

def home(request):
    # # each index has the info of 1 pokemon
    # pokemonList = []
    # # bulbasaur, charmander, squirtle
    # for i in range(1, 4):
    #     response=requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json()

    #     ########## EVOLUTIONS ##########
    #     pokemonEvolutions = []
    #     species_link = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{i}').json()
    #     evolution_link = species_link['evolution_chain']['url']
    #     evolution_chain=requests.get(evolution_link).json()

    #     ## STARTER
    #     tier1 = evolution_chain['chain']['species']['name']
    #     pokemonEvolutions.append(tier1)

    #     ## FIRST EVOLUTION
    #     first_evo = evolution_chain['chain']['evolves_to']
    #     if first_evo:
    #         ## IN CASE OF MULTIPLE EVOLUTIONS
    #         tier2 = []
    #         for evo in range(len(first_evo)):
    #             tier2.append(first_evo[evo]['species']['name'])
    #         tier2 = ':'.join(tier2)
    #         pokemonEvolutions.append(tier2)
            
    #     ## SECOND EVOLUTION
    #         second_evo = first_evo[0]['evolves_to']
    #         if second_evo:
    #             tier3 = []
    #             for evo in range(len(second_evo)):
    #                 tier3.append(second_evo[evo]['species']['name'])
    #             tier3 = ':'.join(tier3)
    #             pokemonEvolutions.append(tier3)
                

    #     ########## TYPES ##########
    #     pokemonTypes = []
    #     for item in response['types']:
    #         typeName = item['type']['name']
    #         pokemonTypes.append(typeName)
    #     pokemonTypes = ':'.join(pokemonTypes)

    #     ########## STATS ##########
    #     statList = []
    #     for i in range(6):
    #         stat = {response['stats'][i]['stat']['name'] : response['stats'][i]['base_stat']}
    #         statList.append(stat)
                
    #     pokemonDict = {
    #     'name': response['name'],
    #     'id': response['id'],
    #     'sprite': response['sprites']['other']['dream_world']['front_default'],
    #     'height' : response['height'], # dm, /10 = m
    #     'weight' : response['weight'], # dag, /10 = kg
    #     'evolutions': pokemonEvolutions,
    #     'types': pokemonTypes,
    #     'stats': statList,
    #     }

    #     pokemonList.append(pokemonDict)
    # context = {'pokemonList': pokemonList}
    pokemons = Pokemon.objects.all()
    context = {'pokemons': pokemons}
    return render(request, 'components/home.html', context)

def login(request):
    return render(request, 'components/login_register.html')