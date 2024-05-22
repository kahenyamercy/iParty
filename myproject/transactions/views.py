from django.shortcuts import render, redirect
from .models import Transaction
from django.shortcuts import get_object_or_404

def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    context = {'transaction': transaction}
    return render(request, 'transaction_detail.html', context)
