import json
import random
from MovesDatabase import MoveList_df
import os

dir_js = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(dir_js, "pokemons.json"), "r", encoding="utf-8") as f:
    pokemons_data = json.load(f)

def pick_moves(pokemon_types, n=2):
    allowed_types = set(t for t in pokemon_types) | {"normal"}
    #pool = [name for name, move in MovesDatabase.MovesList.items() if move[1] in allowed_types and move[3] is not None and move[5] is not None]
    print(allowed_types)
    print(MoveList_df["type"])
    pool = MoveList_df[MoveList_df["type"].isin(allowed_types) & MoveList_df["power"].notna() & MoveList_df["accuracy"].notna()]
    print(pool)
    return tuple(random.sample(pool, min(n, len(pool))))


PokemonList = {
    name: [
        data[0],  # pokedex
        data[1],  # names
        tuple(data[2]),  # types
        data[3],  # base stats
        pick_moves(data[2])  # moves
    ]
    for name, data in pokemons_data.items()
}