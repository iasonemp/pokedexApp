from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('populate/', views.populatePokemonDatabase, name="populate"),
    path('detail/<str:pokemon_name>', views.detail, name="detail"),
    path('api/search/', views.search, name='search')
]