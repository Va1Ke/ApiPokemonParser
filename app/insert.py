import asyncio
import json
from app.cruds.pokemonCruds import PokemonCruds
from app.database import db


async def add_all_pokemons_to_db():
    with open('data.json') as json_file:
        data = json.load(json_file)
    await PokemonCruds(db=db).add_pokemons(data)


async def main():
    await db.connect()
    await add_all_pokemons_to_db()
    await db.disconnect()


asyncio.run(main())
