import googlemaps
import json
import requests

test_args = {'key': "AIzaSyCuutZJ6_u2Lb8l2WNOJ6zh7BuK_P1CKbU", 'location': '41.801691,-87.5943719', 'rankby': 'distance', 'types': 'cafe'}

def find_places(args):
	r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?", params = args)
	print(r.url)	
	data = r.json()
	return(data)

def parse_places(args):
	places = find_places(args)
	rv = []
	for p in places["results"]:
		lat = p['geometry']['location']['lat']
		lng = p['geometry']['location']['lng']
		coords = str(lat) + "," + str(lng)
		rv.append(coords)
	return rv


