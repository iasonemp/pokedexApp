from django.db import models

class Pokemon(models.Model):
    # CharField
    name = models.CharField(max_length=50)

    starter_form = models.CharField(max_length=50)
    # string
    tier_1_evolution = models.CharField(max_length=255)
    # string:string, nullable
    tier_2_evolution = models.CharField(max_length=255)
    # string:string, nullable
    types = models.CharField(max_length=255)
    # string:string
    
    # ImageField
    sprite = models.ImageField(upload_to='static/images/', null=True)
    # models.ImageField(null=True, default="avatar.svg")
    
    # IntegerField
    pokedex_number = models.IntegerField(unique=True)
    height = models.IntegerField
    weight = models.IntegerField
    hp = models.IntegerField
    attack = models.IntegerField
    defense = models.IntegerField
    speed = models.IntegerField
    special_attack = models.IntegerField
    special_defense = models.IntegerField