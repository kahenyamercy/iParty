from django.db import models
from decimal import Decimal  # For handling monetary values

class Transaction(models.Model):
    booking = models.OneToOneField('bookings.Booking', on_delete=models.CASCADE, related_name='payments')  # One-to-One relationship with Booking
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Store transaction amount
    method = models.CharField(max_length=50, choices=(('cash', 'Cash'), ('card', 'Card'), ('online', 'Online'),))  # Payment method choices
    created_at = models.DateTimeField(auto_now_add=True)  # Transaction creation time
