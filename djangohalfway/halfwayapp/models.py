from django.db import models

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
    participant_one = models.ForeignKey(Participant, related_name = 'participant_one', null = True, blank =  True)
    participant_two = models.ForeignKey(Participant, related_name = 'participant_two', null = True, blank = True)
    business_type = models.CharField(max_length=64, null=True, blank=True, choices = BUSINESS_TYPES)
    trip_id = models.IntegerField(null=True, blank = True)
    destination = models.ForeignKey(Address, null=True, blank = True)

    def get_id(self):
        return self.id

    def hash_id(self):
        hash_val = 0
        for char in self.business_type:
            current = ord(char[0])
            hash_val += ((current + hash_val) * self.id) 
        return hash_val 
    def __str__(self):
        return "%s " % (self.destination)
