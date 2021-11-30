import pandas as pd
import rec

df = pd.read_csv('clinicas.csv', encoding="utf-8-sig")

print(df)

lon = []
lat = []

for x in range(len(df)):
	text = df.loc[x][3]
	gid = df.loc[x][1]
	check = rec.coordenadas(text,gid)
	lon.append(check[0])
	lat.append(check[1])

df['lon'] = lon
df['lat'] = lat

df.to_csv('clinicas_f.csv',encoding='utf-8-sig')
result = df.to_json(orient="records", encoding="utf-8-sig")
parsed = json.loads(result)
print (parsed)
json.dumps(parsed, indent=4)
df.to_json(r'test.json')
	 
