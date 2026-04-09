import json
import os
import pandas as pd
import numpy as np
dir_js = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(dir_js, "moves.json"), "r", encoding="utf-8") as f:
    data = json.load(f)


MoveList_df = pd.DataFrame.from_dict(data, orient='index')


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
#print(MoveList_df)


