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
    trip_id = models.CharField(null=True, blank = True)
    destinations = models.ForeignKey(Address, null=True, blank = True)
    #midpoint = models.ForeignKey()

    def get_id(self):
        return self.id

    def random_words(self):
        rw =  RandomWords()
        w1 = rw.random_word()
        w2 = rw.random_word()
        w3 = rw.random_word()
        return w1 + "-" + w2 + "-" + w3

    def __str__(self):
        return "%s " % (self.destination)