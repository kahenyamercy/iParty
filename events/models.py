from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    campus = models.ForeignKey('campus.Campus', on_delete=models.CASCADE)
    attendees = models.ManyToManyField('users.CustomUser', blank=True, related_name='event_attendees')
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='event_creator')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    poster = models.ImageField(upload_to='event_posters/', blank=True)

    
    
