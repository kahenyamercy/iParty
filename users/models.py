from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    campus = models.ForeignKey('campus.Campus', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    events = models.ManyToManyField('events.Event', blank=True, related_name='user_events')

    # Define your custom fields
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    user_permissions = models.ManyToManyField('auth.Permission', blank=True, related_name='custom_user_permissions')
    groups = models.ManyToManyField('auth.Group', blank=True, related_name='custom_user_groups')
