from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Account, Transaction

def home(request):
    return render(request, 'InfinityFinance/homepage.html')

def error_404(request, exception):
    return render(request, 'InfinityFinance/404.html', status=404)

def account(request):
    # Your logic for account view
    user = request.user
    account = user.account  # Assuming user has a one-to-one relationship with Account model
    transactions = Transaction.objects.filter(account=account)
    return render(request, 'bank/account.html')

def transfer(request):
    # Your logic for transfer view
    if request.method == 'POST':
        # Process transfer form submission
        # Validate transfer details
        # Deduct transfer amount from sender's account
        # Add transfer amount to recipient's account
        # Create transaction records for both accounts
        return redirect('account')  # Redirect to account page after successful transfer
    else:
        # Display transfer form
        return render(request, 'bank/transfer.html')
    
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

def account_details(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    return render(request, 'bank/account_details.html', {'account': account})