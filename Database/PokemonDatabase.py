import json
import random
from .MovesDatabase import MoveList_df
import pandas as pd
import os

dir_js = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(dir_js, "pokemons.json"), "r", encoding="utf-8") as f:
    pokemons_data = json.load(f)

def pick_moves(pokemon_types, n=2):
    allowed_types = set(t for t in pokemon_types) | {"normal"}
    pool = MoveList_df[MoveList_df["type"].isin(allowed_types) & MoveList_df["power"].notna() & MoveList_df["accuracy"].notna()]
    return tuple(random.sample(list(pool.index), min(n, len(pool))))

pokemon_records = []

for name, data in pokemons_data.items():
    pokemon_records.append({
        "name": name,
        "pokedex": data[0],
        "display_name": data[1],
        "types": tuple(data[2]),
        "base_stats": data[3],
        "moves": pick_moves(data[2])
    })
Pokemon_df = pd.DataFrame(pokemon_records).set_index("name")
print(Pokemon_df)