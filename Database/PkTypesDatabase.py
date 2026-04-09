import json
import os
import pandas as pd
dir_js = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(dir_js, "type_effectiveness.json"), "r", encoding="utf-8") as f:
    TYPE_CHART = json.load(f)

type_chart_df = pd.DataFrame(TYPE_CHART)
type_chart_df = type_chart_df.fillna(1)
'''
print(type_chart_df.head())
'''
