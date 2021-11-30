import pandas as pd

df = pd.read_csv('clinicas_f.csv', encoding="utf-8-sig")

padres = df['region'].unique()

print(padres)

region = []
centros = []
newdf = pd.DataFrame()

for x in range(len(padres)):
	
	filtro = df['region'] == padres[x]
	print('filtro:',x)
	df_objetivo = df[filtro]
	print('df filtrado:',df_objetivo)
	region.append(padres[x])
	df_objetivo = df_objetivo.drop(columns=['region', 'gid'])
	centros.append(df_objetivo)

print('region:',region)
print('centros:',centros)

newdf['region'] = region
newdf['centros'] = centros

print(newdf)
	
newdf.to_csv('clinicas_anidado.csv',encoding='utf-8-sig')

import json

result = newdf.to_json(orient="values")
parsed = json.loads(result)
print (parsed)
convert = json.dumps(parsed, indent=4)
print(convert)
newdf.to_json(r'test.json')
