import requests
import json
import time



def coordenadas(text,gid):
	time.sleep(5)
	headers = {
		'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
	}

	text = text
	boundary_gid = gid
	boundary_country = 'CO'


	call = requests.get('https://api.openrouteservice.org/geocode/search?api_key=5b3ce3597851110001cf62483cd67629142c4ff0848f203d81d6d4ee&text='+text+'&boundary.gid='+boundary_gid+'&boundary.country=CO', headers=headers)

	print(call.status_code, call.reason)
	print(call.text)
	
	respuesta = json.loads(call.text)
	
	try:
		lon = respuesta['features'][0]['geometry']['coordinates'][0]
		lat = respuesta['features'][0]['geometry']['coordinates'][1]
	
	except:
		lon = 0.0
		lat = 0.0

	return(lon,lat)

