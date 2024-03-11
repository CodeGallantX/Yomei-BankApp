from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Account, Transaction
from .forms import WithdrawForm, TransferForm, DepositForm
from django.contrib import messages

def home(request):
    return render(request, 'InfinityFinance/homepage.html')

def error_404(request, exception):
    return render(request, 'InfinityFinance/404.html', status=404)

def account(request):
    # Your logic for account view
    user = request.user
    account = user.account  # Assuming user has a one-to-one relationship with Account model
    transactions = Transaction.objects.filter(account=account)
    return render(request, 'InfinityFinance/account.html', {'account': account, 'transactions': transactions})

def transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            # Process transfer
            # Example logic:
            sender_account = request.user.account
            recipient_account = form.cleaned_data['recipient_account']
            amount = form.cleaned_data['amount']
            # Deduct amount from sender's account
            sender_account.balance -= amount
            sender_account.save()
            # Add amount to recipient's account
            recipient_account.balance += amount
            recipient_account.save()
            # Create transaction records for both accounts
            Transaction.objects.create(account=sender_account, amount=-amount)
            Transaction.objects.create(account=recipient_account, amount=amount)
            return redirect('account')
    else:
        form = TransferForm()
    return render(request, 'InfinityFinance/transfer.html', {'form': form})
    
def deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            # Process deposit
            # Example logic:
            account = request.user.account
            amount = form.cleaned_data['amount']
            # Add amount to user's account
            account.balance += amount
            account.save()
            # Create transaction record for the deposit
            Transaction.objects.create(account=account, amount=amount)
            return redirect('account')
    else:
        form = DepositForm()
    return render(request, 'InfinityFinance/deposit.html', {'form': form})
    
def withdraw(request):
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            # Process withdrawal
            # Example logic:
            account = request.user.account
            amount = form.cleaned_data['amount']
            # Check if user has sufficient balance
            if account.balance >= amount:
                # Deduct amount from user's account
                account.balance -= amount
                account.save()
                # Create transaction record for the withdrawal
                Transaction.objects.create(account=account, amount=-amount)
                return redirect('account')
            else:
                # Insufficient balance
                form.add_error('amount', 'Insufficient balance')
    else:
        form = WithdrawForm()
    return render(request, 'InfinityFinance/withdraw.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'InfinityFinance/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'InfinityFinance/register.html'


