from sqlalchemy import Column, String, Integer
from app.database import Base


class Pokemon(Base):
    __tablename__ = "pokemons"
    pokemon_id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False, unique=True)
    hp = Column(Integer, nullable=False)
    attack = Column(Integer, nullable=False)
    defense = Column(Integer, nullable=False)
    special_attack = Column(Integer, nullable=False)
    special_defense = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)


pokemons = Pokemon.__table__
