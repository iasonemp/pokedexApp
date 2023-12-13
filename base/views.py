from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Pokemon, User, Comment
from .forms import MyUserCreationForm, CommentForm
from .repeating_views.get_evolution_data import get_evolution_data
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

def userProfile(request, username):
    # favorites
    # sets of 6
    user = User.objects.get(username=username)
    # favorites = request.user.favorites.all()

    # comments = user.comment_set.all()
    context = {'user': user}
    # , 'favorites': favorites}
    # , 'comments': comments}
    return render(request, 'components/userProfile.html', context)

def pokemonPage(request, pokemon_name):
    pokemon = Pokemon.objects.get(name=pokemon_name) 
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
            messages.error(request, 'An error occurred during registration.')
        
    return render(request, 'components/register.html', {'form': form})

def search(request):
    query = request.GET.get('query', '')
    results = Pokemon.objects.filter(name__icontains=query).values('name')
    print(list(results))
    return JsonResponse({'results': list(results)})


def detail(request, pokemon_name):

    pokemon = Pokemon.objects.get(name=pokemon_name)
    
    starter = Pokemon.objects.get(name=pokemon.starter_form)
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

####################################################################################
# def detail_old(request, pokemon_name): 
#     pokemon = Pokemon.objects.get(name=pokemon_name)
#     starter = Pokemon.objects.get(name=pokemon.starter_form)
    
#     context = {'starter_form': pokemon.starter_form, 
#                'starter_id' : starter.pokedex_number,
#                'starter_type' : starter.types,
#                'tier_1_evolution' : pokemon.tier_1_evolution, 
#                'tier_2_evolution' : pokemon.tier_2_evolution,
#                'starter_sprite' : str(starter.sprite),
#                'types' : pokemon.types,
#                'height' : pokemon.height,
#                'weight' : pokemon.weight,
#                'hp' : pokemon.hp,
#                'attack' : pokemon.attack,
#                'defense' : pokemon.defense,
#                'speed' : pokemon.speed,
#                'special_attack' : pokemon.special_attack,
#                'special_defense' : pokemon.special_defense,
#             }
#     # GET sprite, type, name, id FOR FIRST EVOLUTIONS
#     t1data = {}
#     if pokemon.tier_1_evolution:
#         split_evos = pokemon.tier_1_evolution.split(':')
#         t1sprite = []
#         t1type = []
#         t1name = []
#         t1id = []
#         for evo in range(len(split_evos)):
#             try:
#                 split_evos[evo] = Pokemon.objects.get(name=split_evos[evo])
#                 t1sprite.append(str(split_evos[evo].sprite))
#                 t1type.append(split_evos[evo].types)
#                 t1name.append(split_evos[evo].name)
#                 t1id.append(str(split_evos[evo].pokedex_number))
#             except:
#                 pass
#         t1sprite = 'delimiter'.join(t1sprite)
#         t1type = 'delimiter'.join(t1type)
#         t1name = 'delimiter'.join(t1name)
#         t1id = 'delimiter'.join(t1id)
#         t1data = {'t1sprite' : t1sprite, 't1type' : t1type, 't1name' : t1name, 't1id': t1id}
#     context.update({'t1data' : t1data})
#     # GET sprite, type, name, id FOR SECOND EVOLUTIONS
#     t2data = {}
#     if pokemon.tier_2_evolution:
#         split_evos = pokemon.tier_2_evolution.split(':')
#         t2sprite = []
#         t2type = []
#         t2name = []
#         t2id = []
#         for evo in range(len(split_evos)):
#             try:
#                 split_evos[evo] = Pokemon.objects.get(name=split_evos[evo])
#                 t2sprite.append(str(split_evos[evo].sprite))
#                 t2type.append(split_evos[evo].types)
#                 t2name.append(split_evos[evo].name)
#                 t2id.append(str(split_evos[evo].pokedex_number))
#             except:
#                 pass
#         t2sprite = 'delimiter'.join(t2sprite)
#         t2type = 'delimiter'.join(t2type)
#         t2name = 'delimiter'.join(t2name)
#         t2id = 'delimiter'.join(t2id)
#         t2data = {'t2sprite' : t2sprite, 't2type' : t2type, 't2name' : t2name, 't2id': t2id}
#     context.update({'t2data' : t2data})
#     return JsonResponse(context)

# Create your views here.
def populatePokemonDatabase(request):
    for i in range(62,63):
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
    search_query = request.GET.get('q', '')
    
    # Retrieve all pokemons
    if request.user.is_authenticated:
        if search_query:  # Get the search query from the request parameters
            user_favorites = request.user.favorites.filter(name__icontains=search_query)
            other_pokemons = Pokemon.objects.filter(name__icontains=search_query).exclude(name__in=user_favorites.values('name'))
        else:
            user_favorites = request.user.favorites.all()
            other_pokemons = Pokemon.objects.exclude(name__in=user_favorites.values('name'))
        all_pokemons = list(user_favorites) + list(other_pokemons)
    else: 
        all_pokemons = Pokemon.objects.all()
    
    pokemon_list = []
    for pokemon in all_pokemons:
        pokemon_dict = {
        'name': pokemon.name,
        'sprite': str(pokemon.sprite),
        'pokemon_id': pokemon.pokedex_number,
        'pokemon_type' : pokemon.types.split(':')
        }
        pokemon_list.append(pokemon_dict)
    
    # Set the number of pokemons to be displayed per page
    pokemons_per_page = 3

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

    context = {'pokemons': pokemons}
    return render(request, 'components/home.html', context)