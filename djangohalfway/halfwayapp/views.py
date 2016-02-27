from django.shortcuts import render
#import googlemaps
import csv
import time
import json
import requests
from django.http import HttpResponse
from django import forms
from . import models




# BUSINESS_TYPES = (
#         ("Coffee", "Coffee Shop"),
#         ("Bar", "Bar"),
#         ("Eatery", "Restaurant"),
#         )

class EnterIDForm(forms.Form):
	meeting_id = forms.CharField()
	def validate_trip_id(self):
		if Meeting.objects.filter(trip_id=  meeting_id):
			return trip_id
		else:
			raise forms.ValidationError("Please enter a valid Meeting Trip ID number.")



class AddAddress(forms.ModelForm):
	class Meta:
		model = models.Address
		fields = ["street", "city", "state", "zip_code"]

	

class AddParticipant(forms.ModelForm):
	class Meta:
		model = models.Participant
		fields = ["transit_mode"]
		widgets = {
			'transit_mode': forms.Select(),
		}


class AddMeeting(forms.ModelForm):
	class Meta:
		model = models.Meeting
		fields = ["business_type"]
		widgets = {
			'business_type': forms.Select(),
		}

def home(request):
	if request.method == 'POST':
		address = AddAddress(request.POST)
		participant = AddParticipant(request.POST)
		meeting = AddMeeting(request.POST)

		if address.is_valid() and participant.is_valid() and meeting.is_valid():
			address_obj = address.save()
			part_obj = participant.save()
			part_obj.starting_location = address_obj
			part_obj.save()

			meeting_obj = meeting.save()
			meeting_obj.participant_one = part_obj
			meeting_obj.trip_id = meeting_obj.hash_id()
			meeting_obj.save()

			c =  {
				'uniq': meeting_obj.trip_id
			}
			return render(request,'halfwayapp/response.html',c)

	else:
		address = AddAddress()
		participant = AddParticipant()
		meeting = AddMeeting()

	c = {
		'forms': [address, participant, meeting],
	}

	return render(request, 'halfwayapp/home.html', c)

def personA(request, address, participant, meeting):
	address_obj = address.save()
	part_obj = participant.save()
	part_obj.starting_location = address_obj
	part_obj.save()

	meeting_obj = meeting.save()
	meeting_obj.participant_one = part_obj
	meeting_obj.trip_id = meeting_obj.hash_id()
	meeting_obj.save()

	c =  {
		'uniq': meeting_obj.trip_id
	}
	return render(request,'halfwayapp/response.html',c)

def respond(request):
	if request.method == 'POST':
		trip_id = GetMeetingID(request.Post)
		# address = AddAddress(request.POST)
		# participant = AddParticipant(request.POST)
		# meeting = AddMeeting(request.POST)
		# if address.is_valid() and participant.is_valid() and meeting.is_valid():
		# 	address_obj = address.save()
		# 	part_obj = participant.save()
		# 	part_obj.starting_location = address_obj
		# 	part_obj.save()

		# 	meeting_obj = meeting.save()
		# 	meeting_obj.participant_one = part_obj
		# 	meeting_obj.trip_id = meeting_obj.hash_id()
		# 	meeting_obj.save()

		# 	c =  {
		# 		'uniq': meeting_obj.trip_id
		# 	}
		# 	return render(request,'halfwayapp/response.html',c)
	# else:
	# 	address = AddAddress()
	# 	participant = AddParticipant()
	# 	meeting = AddMeeting()
	c = {
		'forms': [GetMeetingID]
	}

	


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
