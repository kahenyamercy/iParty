from django.db import models
from ipartyapp.users.models import User
from ipartyapp.campus.models import Campus

class Event(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    attendees = models.ManyToManyField(User, related_name='events')

    def __str__(self):
        return f"{self.location} - {self.date} - {self.time}"
