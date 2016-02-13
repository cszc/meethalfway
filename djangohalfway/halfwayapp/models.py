from django.db import models

class Address(models.Model):
    street = models.CharField(max_length = 64)
    city = models.CharField(max_length = 64)
    state = models.CharField(max_length = 2)
    zip_code = models.CharField(max_length = 5)

class Participant(models.Model):
    starting_location = models.ForeignKey(Address)
    transit_mode = models.TextField(max_length = 70)

class Meeting(models.Model):
    participant_one = models.ForeignKey(Participant, related_name = 'Participant_one')
    participant_two = models.ForeignKey(Participant, related_name = 'Participant_two')
    business_type = models.TextField()
    trip_id = models.IntegerField()
    destination = models.ForeignKey(Address)
