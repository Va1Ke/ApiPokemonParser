"""corrected pokemon model

Revision ID: 8374145e6dac
Revises: a0d264ad638a
Create Date: 2023-11-14 09:44:45.192096

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8374145e6dac'
down_revision: Union[str, None] = 'a0d264ad638a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pokemons', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('pokemons', 'hp',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('pokemons', 'attack',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('pokemons', 'defense',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('pokemons', 'special_attack',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('pokemons', 'special_defense',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('pokemons', 'speed',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_unique_constraint(None, 'pokemons', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pokemons', type_='unique')
    op.alter_column('pokemons', 'speed',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pokemons', 'special_defense',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pokemons', 'special_attack',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pokemons', 'defense',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pokemons', 'attack',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pokemons', 'hp',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('pokemons', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###