import json
import os

dir_js = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(dir_js, "moves.json"), "r") as f:
    data = json.load(f)

MovesList = {name: list(move.values()) for name, move in data.items()}
