from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    max_attendees = models.PositiveIntegerField()
    contribution_amount = models.DecimalField(max_digits=10, decimal_places=2)
    campus = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
