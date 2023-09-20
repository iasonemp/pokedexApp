from django.db import models

class Pokemon(models.Model):
    # CharField
    name = models.CharField(max_length=50)

    starter_form = models.CharField(max_length=50)
    # string
    tier_1_evolution = 
    # string:string, nullable
    tier_2_evolution = 
    # string:string, nullable
    
    # ForeignKey
    types = 
    # string:string, foreign key
    
    # ImageField
    sprite = models.ImageField
    # models.ImageField(null=True, default="avatar.svg")
    
    # IntegerField
    pokedex_id = 
    height = 
    weight = 
    hp = 
    attack = 
    defense =
    speed = 
    special_attack = 
    special_defense = 
    
    

    class Type(models.Model):
        name = 
        color = 