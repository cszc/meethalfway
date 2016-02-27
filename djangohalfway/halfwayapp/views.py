from django.shortcuts import render
#import googlemaps
import csv
import time
import json
import requests
from django.http import HttpResponse
from django import forms
from . import models

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
			meeting_obj.trip_id = meeting_obj.random_words()
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
