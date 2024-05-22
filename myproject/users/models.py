from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    campus = models.ForeignKey('campus.Campus', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    events = models.ManyToManyField('events.Event', blank=True, related_name='user_events')
    
