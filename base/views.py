from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Pokemon, User, Comment
from .forms import MyUserCreationForm, CommentForm
from .repeating_views.get_evolution_data import get_evolution_data
from .enums import PokemonTypes
import json
import os
import requests
    
@login_required
def deleteComment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return JsonResponse({'status': 'success', 'comment_id': comment_id})

def removeFavoritePokemon (request, pokemon_name):
    pokemon = Pokemon.objects.get(name=pokemon_name)
    request.user.favorites.remove(pokemon)
    return JsonResponse({'status': 'success'})

def addFavoritePokemon (request, pokemon_name):
    pokemon = Pokemon.objects.get(name=pokemon_name)
    request.user.favorites.add(pokemon)
    return JsonResponse({'status': 'success'})

def pokemonPage(request, pokemon_name):
    pokemon = Pokemon.objects.get(name=pokemon_name) 
    # height from dm to cm
    pokemon.height *= 10
    pokemon.height = str(pokemon.height) + 'cm'
    # weight from dg to kg
    pokemon.weight /= 10
    pokemon.weight = str(pokemon.weight) + 'kg'
    pokemon.types = pokemon.types.split(':')
    if request.user.is_authenticated:
        is_favorited = request.user.favorites.filter(name=pokemon_name).exists()
    else:
        is_favorited = False
    comments = Comment.objects.filter(pokemon=pokemon)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.pokemon = pokemon
            comment.body = request.POST.get('body')
            comment.save()
            form = CommentForm()
    else:
        form = CommentForm()
    
    context = {'form': form, 'pokemon':pokemon, 'comments': comments, 
               'is_favorited': is_favorited}
    
    return render(request, 'components/pokemonPage.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist.')
    context = {}
    return render(request, 'components/loginPage.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            errors = form.errors

            # We return only the first error
            first_error = next(iter(errors.values()))[0]
            messages.error(request, first_error)
        
    return render(request, 'components/register.html', {'form': form})


# pokemon type search
def type_search(request):
    body = json.loads(request.body)
    pokemon_type_search_input = body['pokemonType']
    pokemon_types = list(map(lambda x: x.value, PokemonTypes))
    type_search_results = []
    for pokemon_type in pokemon_types:
        if pokemon_type_search_input.lower() in pokemon_type.lower():
            type_search_results.append(pokemon_type)
    
    return JsonResponse({'results': type_search_results})

# pokemon name search
def name_search(request):
    query = request.GET.get('query', '')
    results = Pokemon.objects.filter(name__icontains=query).values('name')
    
    return JsonResponse({'results': list(results)})


def detail(request, pokemon_name):
    pokemon = Pokemon.objects.get(name=pokemon_name)
    
    context = {'name': pokemon.name,
               'sprite': str(pokemon.sprite),
               'pokemon_id': pokemon.pokedex_number,
               'tier_1_evolution' : pokemon.tier_1_evolution, 
               'tier_2_evolution' : pokemon.tier_2_evolution,
               'types' : pokemon.types,
               'height' : pokemon.height,
               'weight' : pokemon.weight,
               'hp' : pokemon.hp,
               'attack' : pokemon.attack,
               'defense' : pokemon.defense,
               'speed' : pokemon.speed,
               'special_attack' : pokemon.special_attack,
               'special_defense' : pokemon.special_defense,
            }
    evo_data = get_evolution_data(pokemon_name)
    context.update({'evo_data': evo_data})
    return JsonResponse(context)

@login_required
def populatePokemonDatabase(request):
    admin_username = os.environ.get('ADMIN_USERNAME')
    if request.user.username == admin_username:
        for i in range(1013, 1014):
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
                else:
                    tier_2_evolution = ''  
            
            else:
                tier_1_evolution = ''
                tier_2_evolution = ''
        
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
                sprite = response['sprites']['other']['official-artwork']['front_default'],
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
    else:
        return redirect('home')

def home(request):
    # search_query = request.GET.get('q', '')
    search_query = request.GET
    name_query = None
    type_query = None
    # Authenticated name search
    if request.user.is_authenticated and 'name' in search_query.keys() and 'type' not in search_query.keys():
        print(request.user.is_authenticated)
        name_query = search_query.get('name')
        user_favorites = request.user.favorites.filter(name__icontains=name_query)
        other_pokemons = Pokemon.objects.filter(name__icontains=name_query).exclude(name__in=user_favorites.values('name'))
        all_pokemons = list(user_favorites) + list(other_pokemons)
    # Authenticated type search
    elif request.user.is_authenticated and 'type' in search_query.keys() and 'name' not in search_query.keys(): 
        type_query = search_query.get('type')
        user_favorites = request.user.favorites.filter(types__icontains=type_query)
        other_pokemons = Pokemon.objects.filter(types__icontains=type_query).exclude(name__in=user_favorites.values('name'))
        all_pokemons = list(user_favorites) + list(other_pokemons)
    # Authenticated all pokemons
    elif request.user.is_authenticated:
        user_favorites = request.user.favorites.all()
        other_pokemons = Pokemon.objects.exclude(name__in=user_favorites.values('name'))
        all_pokemons = list(user_favorites) + list(other_pokemons)
    # Unauthenticated name search
    elif 'name' in search_query.keys() and 'type' not in search_query.keys():
        name_query = search_query.get('name')
        all_pokemons = Pokemon.objects.filter(name__icontains=name_query)
    # Unauthenticated type search
    elif 'type' in search_query.keys() and 'name' not in search_query.keys():
        type_query = search_query.get('type')
        all_pokemons = Pokemon.objects.filter(types__icontains=type_query)
    else:
        all_pokemons = Pokemon.objects.all()
    pokemon_list = []
    for pokemon in all_pokemons:
        pokemon_id = str(pokemon.pokedex_number)
        if len(pokemon_id) == 1:
            pokemon_id = '000' + pokemon_id
        elif len(pokemon_id) == 2:
            pokemon_id = '00' + pokemon_id
        elif len(pokemon_id) == 3:
            pokemon_id = '0' + pokemon_id
        else:
            continue
        
        pokemon_dict = {
        'name': pokemon.name,
        'sprite': str(pokemon.sprite),
        'pokemon_id': pokemon_id,
        'pokemon_type' : pokemon.types.split(':')
        }
        pokemon_list.append(pokemon_dict)
    
    # Set the number of pokemons to be displayed per page
    pokemons_per_page = 15

    # Use Django's Paginator to paginate the queryset
    paginator = Paginator(pokemon_list, pokemons_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page', 1)

    try:
        # Get the paginated pokemons for the current page
        pokemons = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        pokemons = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page
        pokemons = paginator.page(paginator.num_pages)

    context = {'pokemons': pokemons, 'type_query': type_query, 'name_query': name_query}
    # print(search_query)
    return render(request, 'components/home.html', context)