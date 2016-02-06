from django.shortcuts import render
import googlemaps
import csv
import time
import json
import requests

#Use different key
gmaps = googlemaps.Client(key='enter key here')

#via driving
def get_matrix_via_car(client, origins, destinations, mode='driving'):
    matrix = client.distance_matrix(origins, destinations)
    return matrix

#via public transportation
def get_matrix_via_transit(client, origins, destinations, mode='transit'):
    matrix = client.distance_matrix(origins, destinations)
    return matrix

def get_rows(distance_matrix):
    '''
    takes a list of dicts returned by google distance matrix call
    '''
    rows = []
    for i, address in enumerate(distance_matrix['origin_addresses']):
        for i, e in enumerate(distance_matrix['rows'][i]['elements']):
            rows.append({
                'origin': address,
                'destination': car_times['destination_addresses'][i],
                'distance1': e['distance']['text'],
                'distance2': e['distance']['value'],
                'duration1': e['duration']['text'],
                'duration2': e['duration']['value'],
                'status': e['status']
                })
    return rows


test_args = {'key': API_KEY, 'location': '41.801691,-87.5943719', 'rankby': 'distance', 'types': 'cafe'}

def find_places(args):
	r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?", params = args)
	print(r.url)
	data = r.json()
	return(data)

