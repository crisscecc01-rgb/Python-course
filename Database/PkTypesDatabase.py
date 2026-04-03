import json
import os

dir_js = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(dir_js, "type_effectiveness.json"), "r") as f:
    TYPE_CHART = json.load(f)
