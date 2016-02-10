from django.contrib import admin

from .models import Address, Participant, Meeting

admin.site.register(Address, Participant, Meeting)
