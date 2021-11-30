import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.famisanar.com.co/oficinas-famisanar-pos/'

respuesta = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'})
soup = BeautifulSoup(respuesta.text, 'html.parser')
#print(soup)

mydivs = soup.find_all("div", {"class": "fusion-clearfix"})

#print(mydivs)

mydivs = soup.find_all("td",{"align":"left"})

#print(mydivs)

for mydiv in mydivs:
	print(mydiv.text)

df = pd.DataFrame()

lines = []
with open('text.txt') as f:
    lines = f.readlines()

direccion = []
telefono = []
horario = []
autorizaciones = []
servicio_al_usuario = []
orientacion_comercial = []

print(len(lines))

for x in range(0,len(lines),6):
	direccion.append(lines[x])

for x in range(1,len(lines),6):
	telefono.append(lines[x])

for x in range(2,len(lines),6):
	horario.append(lines[x])
	
for x in range(3,len(lines),6):
	autorizaciones.append(lines[x])

for x in range(4,len(lines),6):
	servicio_al_usuario.append(lines[x])

for x in range(5,len(lines),6):
	orientacion_comercial.append(lines[x])

print (direccion)
df['direccion'] = direccion
df['telefono'] = telefono
df['horario'] = horario
df['autorizaciones'] = autorizaciones
df['servicio_al_usuario'] = servicio_al_usuario
df['orientacion_comercial'] = orientacion_comercial

print(df)

df.to_csv('clinicas.csv',encoding='utf-8-sig')


