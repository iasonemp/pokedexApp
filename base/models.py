from django.db import models
from django.contrib.auth.models import AbstractUser
    

class Pokemon(models.Model):
    # CharField
    name = models.CharField(max_length=100)

    starter_form = models.CharField(max_length=100)
    # string
    tier_1_evolution = models.CharField(max_length=255, blank=True, null=True, default=None)
    # string:string, nullable
    tier_2_evolution = models.CharField(max_length=255, blank=True, null=True, default=None)
    # string:string, nullable
    types = models.CharField(max_length=255)
    # string:string
    
    # ImageField
    sprite = models.ImageField(upload_to='static/images/', blank=True, null=True, default=None)
    # models.ImageField(null=True, default="avatar.svg")
    
    # IntegerField
    pokedex_number = models.IntegerField(unique=True)
    height = models.IntegerField(blank=True, null=True, default=None)
    weight = models.IntegerField(blank=True, null=True, default=None)
    hp = models.IntegerField(blank=True, null=True, default=None)
    attack = models.IntegerField(blank=True, null=True, default=None)
    defense = models.IntegerField(blank=True, null=True, default=None)
    speed = models.IntegerField(blank=True, null=True, default=None)
    special_attack = models.IntegerField(blank=True, null=True, default=None)
    special_defense = models.IntegerField(blank=True, null=True, default=None)
    
    def __str__(self):
        return self.name
    
class User(AbstractUser):
    username = models.CharField(unique=True, max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    favorites = models.ManyToManyField(Pokemon, related_name='favorited_by')

    # λογικα εδω θα μπουν αργοτερα και τα sets

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.username} - {self.pokemon.name} - {self.created}'