from django.db import models
from ipartyapp.event.models import Event
from ipartyapp.users.models import User
from ipartyapp.transaction.models import Transaction

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} booked {self.event.name}"
