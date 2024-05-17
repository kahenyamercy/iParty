from django.db import models
from django.contrib.auth.models import User
from ipartyapp.event.models import Event
from ipartyapp.campus.models import Campus

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    events = models.ManyToManyField(Event, blank=True, related_name='user_events')