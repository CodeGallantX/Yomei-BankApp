from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm

# Create your views here.

def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'transactions/create_transaction.html', {'form': form})

def delete_transaction(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'transactions/delete_transaction.html', {'transaction': transaction})
