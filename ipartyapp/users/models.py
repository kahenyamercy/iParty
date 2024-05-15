from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    CAMPUS_CHOICES = [
        ('Campus A', 'KU'),
        ('Campus B', 'JKUAT'),
        ('Campus C', 'UON'),
    ]

    campus = models.CharField(max_length=100, choices=CAMPUS_CHOICES)
    phone_number = models.CharField(max_length=15)
    mpesa_transaction_code = models.CharField(max_length=20, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        verbose_name=('groups'),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )


class PartyEvent(models.Model):
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='organized_events')

    event_name = models.CharField(max_length=100)

    event_date = models.DateTimeField()

    invitees_number = models.IntegerField()

    contribution_amount = models.DecimalField(max_digits=10, decimal_places=2)

    booked_users = models.ManyToManyField(CustomUser, related_name='booked_events')



class Contribution(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    event = models.ForeignKey(PartyEvent, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    timestamp = models.DateTimeField(auto_now_add=True)

