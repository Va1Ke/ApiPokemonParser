import databases
from app.models.models import pokemons


class PokemonCruds:
    def __init__(self, db: databases.Database):
        self.db = db

    async def add_pokemons(self, pokemon_list: dict) -> dict:
        query = pokemons.insert().values(pokemon_list)
        await self.db.execute(query)
        return {'status': 'success'}
