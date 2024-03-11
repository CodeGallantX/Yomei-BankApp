from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Account, Transaction
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'InfinityFinance/homepage.html')

def error_404(request, exception):
    return render(request, 'InfinityFinance/404.html', status=404)

def account(request):
    # Your logic for account view
    user = request.user
    account = user.account  # Assuming user has a one-to-one relationship with Account model
    transactions = Transaction.objects.filter(account=account)
    return render(request, 'bank/account.html', {'account': account, 'transactions': transactions})

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
    return render(request, 'bank/transfer.html', {'form': form})
    
def deposit(request):
    # Your logic for deposit view
    if request.method == 'POST':
        # Process deposit form submission
        # Validate deposit details
        # Add deposit amount to user's account
        # Create transaction record for the deposit
        return redirect('account')  # Redirect to account page after successful deposit
    else:
        # Display deposit form
        return render(request, 'bank/deposit.html')
    
def withdraw(request):
    # Your logic for withdraw view
    if request.method == 'POST':
        # Process withdrawal form submission
        # Validate withdrawal details
        # Deduct withdrawal amount from user's account
        # Create transaction record for the withdrawal
        return redirect('account')  # Redirect to account page after successful withdrawal
    else:
        # Display withdrawal form
        return render(request, 'bank/withdraw.html')
    

class CustomLoginView(LoginView):
    template_name = 'bank/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

@login_required
def account_details(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    return render(request, 'bank/account_details.html', {'account': account})