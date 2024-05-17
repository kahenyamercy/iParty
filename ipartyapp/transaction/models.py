from django.db import models

class Transaction(models.Model):
    date = models.DateField()
    time = models.TimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference_number = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.reference_number} - {self.amount}"