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


    def get_destinations():
        stuff = None

    def get_potential_destinations(participant):
        #returns pseudo json and dicts
        directions = get_directions(gmaps, participant.address)
        #returns tuple (substeps, time)
        steps_and_time = get_steps_and_time(directions)
        #returns latlongs
        midpoint = get_midpoint(steps_and_time)
        #returns ?
        potential_destinations = find_places(midpoint_a, business_type)

        return potential_destinations
        potential_places = potential_places_a + potential_places_b

        matrix_a = get_matrix(a_address, potential_places)
        matrix_b = get_matrix(b_address, potential_places)

        #function to compare matrix a travel times with b travel times

        #return top 5 best scores, or rereun if scores not good enough

    def get_destinations(address_a, address_b):
        potential_dest_a, latlngs_a = get_potential_destinations(participant_one)
        potential_dest_b, latlngs_b = get_potential_destinations(participant_two)
        potential_latlngs = latlngs_a + latlngs_b
        matrix_a = get_matrix(a_address, potential_latlngs)
        matrix_b = get_matrix(b_address, potential_latlngs)
        get_results(matrix_a, matrix_b)

    def get_results(matrix_one, matrix_two):
        scores = []
        addresses = matrix_a['destination_addresses']
        a_times = matrix_a['rows'][0]['elements']
        b_times = matrix_b['rows'][0]['elements']
        for i, a in enumerate(addresses):
            a_time = a_times[i]['duration']['value']
            b_time = b_times[i]['duration']['value']
            if a_time <= b_time:
                score = 1 - (a_time/b_time)
            else:
                score = 1 - (b_time/a_time)
            scores.append((a, a_time, b_time, score))
        rv = []
        for score in scores:
            if len(rv) < 5:
                if score[3] < 0.2:
                    rv.append(score)
        if len(rv) == 0:
            best_scores = sorted(scores, key=lambda tup: tup[3])
            found_result = False
            return found_result, best_scores[0][0]
        else:
            rv = sorted(rv, key=lambda tup: tup[3])
            found_result = True
            return found_result, rv

    def get_potential_destinations(participant):
        '''
        returns a tuple of potential destinations (dicts) and list of latlongs
        '''
        #returns pseudo json and dicts
        directions = get_directions(gmaps, participant.address)
        #returns tuple (substeps, time)
        steps_and_time = get_steps_and_time(directions)
        #returns latlongs
        midpoint = get_midpoint(steps_and_time)
        #returns ?
        places_dict = something
        potential_destinations = get_places(places_dict)
        return potential_destinations


    def get_directions(client, origin, destination, mode='transit'):
        return client.directions(origin, destination, mode)

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

    def get_places(args):
    	r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?", params = args)
    	data = r.json()
        latlngs = parse_places(data)
    	return(data, latlngs)

    def parse_places(places):
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
