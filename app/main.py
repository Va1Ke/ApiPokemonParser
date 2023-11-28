from app.cruds.pokemonCruds import PokemonCruds
import requests
from app.database import db
import asyncio


def get_stats(pokemons: list):
    pokemons_details = []
    for pokemon in pokemons:
        details = requests.get(pokemon.get('url')).json()
        stats = details.get('stats')
        pokemon_stats = {}
        for stat in stats:
            pokemon_stats.update({stat.get('stat').get('name'): stat.get('base_stat')})
        pokemons_details.append({
            'name': pokemon.get('name'),
            'hp': pokemon_stats.get('hp'),
            'attack': pokemon_stats.get('attack'),
            'defense': pokemon_stats.get('defense'),
            'special_attack': pokemon_stats.get('special-attack'),
            'special_defense': pokemon_stats.get('special-defense'),
            'speed': pokemon_stats.get('speed')
        })
    return pokemons_details


def get_pokemons(url: str):
    response = requests.get(url)
    pokemon_list = get_stats(response.json().get('results'))
    if response.json().get('next'):
        pokemon_list = pokemon_list + get_pokemons(response.json().get('next'))
    return pokemon_list


async def pokemons_to_db(url: str):
    pokemon_list = get_pokemons(url)
    await PokemonCruds(db=db).add_pokemons(pokemon_list)


async def main():
    await db.connect()
    await pokemons_to_db('https://pokeapi.co/api/v2/pokemon')
    await db.disconnect()


asyncio.run(main())
