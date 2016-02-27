import googlemaps
import requests
import csv
import time
import json

with open('apikeys.txt', 'r') as f:
    apikey = f.readline()
gmaps = googlemaps.Client(key=apikey)

start = '121 N LaSalle St, Chicago, IL 60602'
end = 'Harris School of Public Policy, 1155 E 60th St'
transit = 'transit'

def get_directions(client, origin, destination, mode='transit'):
    directions = client.directions(origin, destination, mode)
    return directions

directions = get_directions(gmaps, start, end, transit)

def get_steps_and_time(directions):
    legs = directions[0]['legs']
    time = legs[0]['duration']['value']
    steps = legs[0]['steps']
    substeps = get_substeps(steps)
    return(substeps, time)

def get_substeps(steps):
    substeps = []
    for x in steps:
        if 'steps' in x.keys():
            for substep in x['steps']:
                substeps.append(substep)
        else:
            substeps.append(x)
    return substeps

def bisect(target_time, current_time, step):
    time_left = target_time - current_time
    duration = step['duration']['value']
    start_lat = step['start_location']['lat']
    start_lng = step['start_location']['lng']
    end_lat = step['end_location']['lat']
    end_lng = step['end_location']['lng']
    ratio = time_left / duration
    add_lat = ratio*(end_lat - start_lat)
    add_lng = ratio*(end_lng - start_lng)
    new_lat = start_lat + add_lat
    new_lng = start_lng + add_lng
    return(new_lat, new_lng)

def get_midpoint(steps, total_time):
    target_time = total_time / 2
    current_time = 0
    for step in steps:
        duration = step['duration']['value']
        end_time = current_time + duration
        print(end_time)
        if end_time < target_time:
            current_time = end_time
            continue
        return(bisect(target_time, current_time, step))

steps, time = get_steps_and_time(directions)
midpoint = get_midpoint(steps, time)

test_args = {'key': apikey, 'location': midpoint, 'rankby': 'distance', 'types': 'cafe'}

def get_places(client, query, location, radius = '800'):
    places = client.places(query, location = location, radius = radius)
    return(places)

# def find_places(args):
# 	r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?", params = args)
# 	print(r.url)
# 	data = r.json()
# 	return(data)

print(get_places(gmaps, 'cafe', midpoint))

# print(steps)
# print(' ')
#print(steps, time)
