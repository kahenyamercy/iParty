from django import forms
from .models import Transaction


class CompletedTransactionSerializer(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'balance', 'receiptNumber', 'transactionDate',
                  'phoneNumber', 'fullName', 'booking']
