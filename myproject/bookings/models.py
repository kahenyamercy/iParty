from django.db import models

class Booking(models.Model):
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    payment = models.ForeignKey('transactions.Transaction', on_delete=models.CASCADE, related_name='bookings')