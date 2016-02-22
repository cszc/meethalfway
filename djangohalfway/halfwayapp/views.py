from django.shortcuts import render
#import googlemaps
import csv
import time
import json
import requests
from django.http import HttpResponse
from django import forms
from . import models


class AddAddress(forms.ModelForm):
	class Meta:
		model = models.Address
		fields = ["street", "city", "state", "zip_code"]

class AddParticipant(forms.ModelForm):
	class Meta:
		model = models.Participant
		fields = ["transit_mode"]

class AddMeeting(forms.ModelForm):
	class Meta:
		model = models.Meeting
		fields = ["business_type"]

def home(request):
	if request.method == 'POST':
		address = AddAddress(request.POST)
		participant = AddParticipant(request.POST)
		if address.is_valid() and participant.is_valid():
			address.save()
			participant.starting_location = address
			participant.save()
			return HttpResponse("Your response has been added")
	else:
		address = AddAddress()
		participant = AddParticipant()
	c = {
		'forms': [address, participant],
	}

	return render(request, 'halfwayapp/home.html', c)

class AddressForm(forms.Form):
	street_address = forms.CharField()
	street_named = forms.CharField()
	city = forms.CharField()
	zipcode = forms.CharField()
	mode = forms.ChoiceField(choices=[('driving', 'Driving'), ('public', 'Public transit')])


def Enter_First_Address(request):
	if request.method == 'POST':
		form = AddressForm(request.POST)
		if form.is_valid():
			# Save into the database
			print(form.cleaned_data['city'])

			return HttpResponse('Your response has been added')
	else:
		form = AddressForm()
	c = {'form': form}
	return render(request, 'halfwayapp/form.html', c)



# gmaps = googlemaps.Client(key='enter key here')
#
# #via drstreeiving
# def get_matrix_via_car(client, origins, destinations, mode='driving'):
#	 matrix = client.distance_matrix(origins, destinations)
#	 return matrix
#
# #via public transportation
# def get_matrix_via_transit(client, origins, destinations, mode='transit'):
#	 matrix = client.distance_matrix(origins, destinations)
#	 return matrix
#
# def get_rows(distance_matrix):
#	 '''
#	 takes a list of dicts returned by google distance matrix call
#	 '''
#	 rows = []
#	 for i, address in enumerate(distance_matrix['origin_addresses']):
#		 for i, e in enumerate(distance_matrix['rows'][i]['elements']):
#			 rows.append({
#				 'origin': address,
#				 'destination': car_times['destination_addresses'][i],
#				 'distance1': e['distance']['text'],
#				 'distance2': e['distance']['value'],
#				 'duration1': e['duration']['text'],
#				 'duration2': e['duration']['value'],
#				 'status': e['status']
#				 })
#	 return rows
#
#
# test_args = {'key': API_KEY, 'location': '41.801691,-87.5943719', 'rankby': 'distance', 'types': 'cafe'}
#
# def find_places(args):
# 	r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?", params = args)
# 	print(r.url)
# 	data = r.json()
# 	return(data)
