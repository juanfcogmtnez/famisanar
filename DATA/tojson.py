import pandas as pd
import json

df = pd.read_csv('clinicas_f.csv', encoding="utf-8-sig")

result = df.to_json(orient="index")
parsed = json.loads(result)
print (parsed)
json.dumps(parsed, indent=4)
df.to_json(r'test.json')
