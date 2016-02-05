from django.db import models

class Address(models.Model):
    street = models.TextField()
    city = models.TextField()
    state = models.CharField(max_length = 2)
    zip_code = models.CharField(max_length = 5)

class Participant(models.Model):
    starting_location = models.ForeignKey(Address, on_delete = models.CASCADE)
    transit_mode = models.TextField(max_length = 70)


class Meeting(models.Model):
    participant_one = models.ForeignKey(Participant, on_delete = models.CASCADE)
    participant_two = models.ForeignKey(Participant, on_delete = models.CASCADE)
    business_type = models.TextField()
    private = models.NullBooleanField()
    trip_id = models.IntegerField()
    url =
    destination = models.ForeignKey(Address, on_delete = models.CASCADE)
