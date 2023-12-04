from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('user/<str:username>/', views.userProfile, name="user-profile"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('populate/', views.populatePokemonDatabase, name="populate"),
    path('detail/<str:pokemon_name>', views.detail, name="detail"),
    path('api/search/', views.search, name='search'),
    path('pokemon/<str:pokemon_name>/', views.pokemonPage, name='pokemonPage'),
    path('add_favorite/<str:pokemon_name>/', views.addFavoritePokemon, name='add_favorite'),
    path('remove_favorite/<str:pokemon_name>/', views.removeFavoritePokemon, name='remove_favorite'),
]