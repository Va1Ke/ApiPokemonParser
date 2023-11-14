import json
import requests


def get_pokemons(url: str, pokemon_list: list, counter: int):
    response = requests.get(url)
    for pokemon in response.json().get('results'):
        details = requests.get(pokemon.get('url')).json()
        stats = details.get('stats')
        pokemon_stats = {}
        for stat in stats:
            pokemon_stats.update({stat.get('stat').get('name'): stat.get('base_stat')})
        pokemon_list.append({
            'name': pokemon.get('name'),
            'hp': pokemon_stats.get('hp'),
            'attack': pokemon_stats.get('attack'),
            'defense': pokemon_stats.get('defense'),
            'special_attack': pokemon_stats.get('special-attack'),
            'special_defense': pokemon_stats.get('special-defense'),
            'speed': pokemon_stats.get('speed')
            })
    if response.json().get('next'):
        get_pokemons(response.json().get('next'), pokemon_list, counter + 1)


def store_all_pokemons_to_file(url: str):
    pokemon_list = []
    get_pokemons(url, pokemon_list, 1)
    with open('data.json', 'w') as f:
        json.dump(pokemon_list, f)


store_all_pokemons_to_file('https://pokeapi.co/api/v2/pokemon/')
