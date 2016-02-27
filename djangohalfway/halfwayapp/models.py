from django.db import models
import googlemaps
import requests
import json
import time
from random_words import RandomWords

with open('apikeys.txt', 'r') as f:
    apikey = f.readline()

gmaps = googlemaps.Client(key=apikey)

class Address(models.Model):
    street = models.CharField(max_length = 64)
    city = models.CharField(max_length = 64)
    state = models.CharField(max_length = 2)
    zip_code = models.CharField(max_length = 5)
    def __str__(self):
        return "%s %s" % (self.street, self.city)

class Participant(models.Model):
    TRANSIT_TYPES = (
        ("Walk", "Walking"),
        ("Public Transit", "Public Transit"),
        ("Car", "Driving"),
        )
    starting_location = models.ForeignKey(Address, null=True, blank = True)
    transit_mode = models.CharField(max_length = 70, choices = TRANSIT_TYPES)

    # def __str__(self):
    #     return "%s %s" % (self.starting_location, self.transit_mode)
    def get_id(self):
        return self.id

class Meeting(models.Model):
    BUSINESS_TYPES = (
        ("Coffee", "Coffee Shop"),
        ("Bar", "Bar"),
        ("Eatery", "Restaurant"),
        )
    participant_one = models.ForeignKey(
        Participant, related_name = 'participant_one', null = True, blank =  True)
    participant_two = models.ForeignKey(
        Participant, related_name = 'participant_two', null = True, blank = True)
    business_type = models.CharField(
        max_length=64, null=True, blank=True, choices = BUSINESS_TYPES)
    trip_id = models.IntegerField(null=True, blank = True)
    destinations = models.ForeignKey(Address, null=True, blank = True)

    def get_id(self):
        return self.id

    def hash_id(self):
        hash_val = 0
        for char in self.business_type:
            current = ord(char[0])
            hash_val += ((current + hash_val) * self.id)
        return hash_val

    def random_words(self):
        rw =  RandomWords()
        w1 = rw.random_word()
        w2 = rw.random_word()
        w3 = rw.random_word()
        return w1 + "-" + w2 + "-" + w3

    def __str__(self):
        return "%s " % (self.destination)

    # def get_destinations():
    #     stuff = None

    # def get_potential_destinations(participant):
    #     #returns pseudo json and dicts
    #     directions = get_directions(gmaps, participant.address)
    #     #returns tuple (substeps, time)
    #     steps_and_time = get_steps_and_time(directions)
    #     #returns latlongs
    #     midpoint = get_midpoint(steps_and_time)
    #     #returns ?
    #     potential_destinations = find_places(midpoint_a, business_type)

    #     return potential_destinations
    #     potential_places = potential_places_a + potential_places_b

    #     matrix_a = get_matrix(a_address, potential_places)
    #     matrix_b = get_matrix(b_address, potential_places)

    #     #function to compare matrix a travel times with b travel times

    #     #return top 5 best scores, or rereun if scores not good enough

    def get_directions(client, origin, destination, mode='transit'):
        directions = client.directions(origin, destination, mode)
        return directions

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

    def get_places(client, location,  query = '', radius = '800', open_now = False, types = None):
        places = client.places(
            query = query,
            location = location,
            radius = radius,
            open_now = False,
            types = types)
        return(places)
    #
    # def find_places(args):
    # 	r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?", params = args)
    # 	print(r.url)
    # 	data = r.json()
    # 	return(data)

    def parse_places(args):
    	places = find_places(args)
    	rv = []
    	for p in places["results"]:
    		lat = p['geometry']['location']['lat']
    		lng = p['geometry']['location']['lng']
    		coords = str(lat) + "," + str(lng)
    		rv.append(coords)
    	return rv

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
