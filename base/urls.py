from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('populate/', views.populatePokemonDatabase, name="populate"),
    path('detail/<str:pokemon_name>', views.detail, name="detail"),
    path('api/name_search/', views.name_search, name='name_search'),
    path('api/type_search/', views.type_search, name='type_search'),
    path('pokemon/<str:pokemon_name>/', views.pokemonPage, name='pokemonPage'),
    path('add_favorite/<str:pokemon_name>/', views.addFavoritePokemon, name='add_favorite'),
    path('remove_favorite/<str:pokemon_name>/', views.removeFavoritePokemon, name='remove_favorite'),
    path('delete_comment/<str:comment_id>/', views.deleteComment, name="delete_comment"),
]