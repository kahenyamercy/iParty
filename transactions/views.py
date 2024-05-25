from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Transaction

def transaction_list(request):
    transactions = Transaction.objects.all()
    context = {'transactions': transactions}
    return render(request, 'transaction_list.html', context)

def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    context = {'transaction': transaction}
    return render(request, 'transaction_detail.html', context)
