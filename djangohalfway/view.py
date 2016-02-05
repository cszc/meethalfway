import json
import requests


test_args = {'key': API_KEY, 'location': '41.801691,-87.5943719', 'rankby': 'distance', 'types': 'cafe'}

def find_places(args):
	r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?", params = args)
	print(r.url)
	data = r.json()
	return(data)

def 
