from django.db import models
from django.utils.timezone import now

class Booking(models.Model):
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    payment = models.ForeignKey('transactions.Transaction', on_delete=models.SET_NULL, null=True, related_name='bookings')
    created_at = models.DateTimeField(default=now)