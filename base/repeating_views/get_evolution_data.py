from ..models import Pokemon

def get_evolution_data(pokemon_name):
    pokemon = Pokemon.objects.get(name=pokemon_name)
    starter = Pokemon.objects.get(name=pokemon.starter_form)
    evo_data = {}
    if pokemon.tier_1_evolution:
            
        all_evos = pokemon.tier_1_evolution + ':' + pokemon.tier_2_evolution
        split_evos = all_evos.split(':')
        evo_sprite = []
        evo_type = []
        evo_name = []
        evo_id = []
        evo_status = []
        for evo in range(len(split_evos)):
            try:
                split_evos[evo] = Pokemon.objects.get(name=split_evos[evo])
                evo_sprite.append(str(split_evos[evo].sprite))
                evo_type.append(split_evos[evo].types)
                evo_name.append(split_evos[evo].name)
                evo_id.append(str(split_evos[evo].pokedex_number))
                if split_evos[evo].name in pokemon.tier_1_evolution:
                    evo_status.append('tier_1')
                else:
                    evo_status.append('tier_2')
            except:
                pass
        evo_sprite = 'delimiter'.join(evo_sprite)
        evo_type = 'delimiter'.join(evo_type)
        evo_name = 'delimiter'.join(evo_name)
        evo_id = 'delimiter'.join(evo_id)
        evo_status = 'delimiter'.join(evo_status)
        evo_data = {'evo_sprite' : evo_sprite, 'evo_type' : evo_type, 
                    'evo_name' : evo_name, 'evo_id': evo_id,
                    'evo_status' : evo_status, 'starter_name': starter.name,
                    'starter_form': pokemon.starter_form,'starter_id' : starter.pokedex_number,
                    'starter_type' : starter.types, 'starter_sprite' : str(starter.sprite),
        }
        
    return evo_data

