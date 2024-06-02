from django.db import models
from django.utils.timezone import now

class Booking(models.Model):
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username