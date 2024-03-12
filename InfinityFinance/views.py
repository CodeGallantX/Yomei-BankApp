from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Account, Transaction, AccountDetails, Wallet, Transaction, Bill, AirtimePurchase
from .forms import WithdrawForm, TransferForm, DepositForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


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
    def form_valid(self, form):
        # Save the user's name to the database
        form.instance.name = form.cleaned_data['name']
        return super().form_valid(form)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('account_details')  # Redirect to account details page
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


@login_required
def dashboard(request):
    user = request.user
    wallet = Wallet.objects.get(user=user)
    transactions = Transaction.objects.filter(wallet=wallet)
    bills = Bill.objects.filter(user=user)
    airtime_purchases = AirtimePurchase.objects.filter(user=user)
    context = {
        'wallet': wallet,
        'transactions': transactions,
        'bills': bills,
        'airtime_purchases': airtime_purchases
    }
    return render(request, 'dashboard.html', context)

def transfer_money(request):
    # Implement money transfer logic here
    pass

def pay_bill(request):
    # Implement bill payment logic here
    pass

def buy_airtime(request):
    # Implement airtime purchase logic here
    pass

def contact(request):
    return render(request, 'InfinityFinance/contact.html')

def thank_you(request):
    return render(request, 'InfinityFinance/thank_you.html')

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Send email to admin
        send_mail(
            f'New message from {name}',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],  # Replace with your admin's email address
            fail_silently=False,
        )
        
        # Redirect the user to a thank you page or the home page
        return HttpResponseRedirect(reverse('thank_you'))
    else:
        return HttpResponseRedirect(reverse('contact'))  # Redirect if not a POST request
