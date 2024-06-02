from django.db import models

class Transaction(models.Model):
    booking = models.OneToOneField('bookings.Booking', on_delete=models.CASCADE, related_name='payments')
    amount = models.IntegerField(default=0)
    receiptNumber = models.CharField(max_length=150, null=True, default=None)
    balance = models.IntegerField(default=0)
    transactionDate = models.CharField(max_length=255, null=True, default=None)
    phoneNumber = models.CharField(max_length=255, null=True, default=None)
    fullName = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
