from sqlite3 import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
# from .models import UserProfile, Bill, AirtimePurchase
from .models import Transactions, Wallet
from .forms import WithdrawForm, TransferForm, DepositForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import random


def home(request):
    return render(request, 'InfinityFinance/homepage.html')

def error_404(request, exception):
    return render(request, 'InfinityFinance/404.html', status=404)

def transfer_funds(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            # Process the form data and perform the transfer operation
            user_account = form.cleaned_data['user_account']
            recipient_account = form.cleaned_data['recipient_account']
            amount = form.cleaned_data['amount']
            recipient_bank_name = form.cleaned_data['recipient_bank_name']
            
            # Assuming you have the sender and recipient objects based on their account numbers
            sender_wallet = Wallet.objects.get(account_number=user_account)
            recipient_wallet = Wallet.objects.get(account_number=recipient_account)

            # Check if sender has enough balance
            if sender_wallet.balance >= amount:
                # Deduct amount from sender's wallet
                sender_wallet.balance -= amount
                sender_wallet.save()

                # Add amount to recipient's wallet
                recipient_wallet.balance += amount
                recipient_wallet.save()

                # Record the transaction
                Transactions.objects.create(sender=sender_wallet.user, recipient=recipient_wallet.user, amount=amount)

                messages.success(request, 'Transfer successful!')
                return redirect('transactions')  # Redirect to transactions page after successful transfer
            else:
                messages.error(request, 'Insufficient balance.')
    else:
        form = TransferForm()
    
    return render(request, 'transactions.html', {'form': form})



'''
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
    return render(request, 'InfinityFinance/withdraw.html', {'form': form})'''





'''
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page or dashboard after successful registration
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'InfinityFinance/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('dashboard')  # Redirect to account details page
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')'''



def dashboard(request):
    user = request.user
   # wallet = Wallet.objects.get(user=user)
    #transactions = Transaction.objects.filter(wallet=wallet)
    #bills = Bill.objects.filter(user=user)
    #airtime_purchases = AirtimePurchase.objects.filter(user=user)

    try:
        wallet = Wallet.objects.get(user=user)
    except Wallet.DoesNotExist:
        # Create a new wallet if it doesn't exist for the user
        wallet = Wallet.objects.create(user=user, account_number="3018725946")  # You may generate a unique account number here
    context = {
        'wallet': wallet,
        #'transactions': transactions,
        #'bills': bills,
        #'airtime_purchases': airtime_purchases
    }
    return render(request, 'InfinityFinance/dashboard.html', context)

'''
def transfer(request):
    # Implement money transfer logic here
    return render(request, 'InfinityFinance/transfer.html')

def pay_bill(request):
    # Implement bill payment logic here
    return render(request, 'bills.html')

def buy_airtime(request):
    # Implement airtime purchase logic here
    return render(request, 'buy-airtime.html')'''

def contact(request):
    return render(request, 'InfinityFinance/contact.html')

def thank_you(request):
    return render(request, 'InfinityFinance/thank_you.html')

def blog(request):
    return render(request, "InfinityFinance/blog.html")

def pricing(request):
    return render(request, "InfinityFinance/pricing.html")

'''def send_email(request):
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
        return HttpResponseRedirect(reverse('contact'))  # Redirect if not a POST request'''



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        username = request.POST['username']  # Add this line to get the username

        try:
            user = User.objects.create_user(username=username, password=pass1, first_name=first_name, last_name=last_name, email=email)
            messages.success(request, 'Your account has been successfully created!')
            return redirect('dashboard')
        except IntegrityError:
            messages.error(request, "Username already exists")
            return redirect('register')

    return render(request, 'InfinityFinance/register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')  # Assuming password field is named 'pass1'

        # Authenticate user
        user = authenticate(request, email=username, password=password)

        if user is not None:
            # Display error message if authentication failed
            messages.error(request, "Invalid username or password.")
            return redirect('home')  # Assuming 'home' is the name of the URL pattern for the home page
           
        else:
            # Login user if authentication successful
            login(request, user)
            user = user.username  # Accessing user's email address
            return render(request, 'InfinityFinance/dashboard.html', {'username':username})

    # If request method is not POST, render the login page
    return render(request, 'InfinityFinance/login.html')


def signout(request):
    logout(request)  # Call the logout function to log out the user
    messages.success(request, "Logged out successfully!!")
    return redirect('home')


def withdraw(request):
    if cur_customer is None:
        # Handle the case when cur_customer is None
        # Redirect the user to an appropriate page or display an error message
        return HttpResponse("Error: No customer information found. Please try again.")

    accounts = cur_customer.accounts
    msg="<br>Enter a valid account no. and also check for ur balance!</p><br>"
    if request.method == "POST":
        acc_num=int(request.POST.get('acc_no'))
        amount=int(request.POST.get('amount'))
        print('requestPOST=',acc_num,type(acc_num))
        #print('account dict:',accounts.keys())
        if acc_num in accounts:
            #acc_obj= accounts[acc_num]
            acc_q=Account_Data.objects.get(Accno=acc_num)
            balance=acc_q.Balance
            print("balance:",balance)
            if(balance>=amount):
                trans=Classes.Account(acc_q)
                trans.create_transaction(amount,"withdraw")
                balance-=amount
                acc_q.Balance=balance
                print("balance:",acc_q.Balance)
                acc_q.save()
                cur_customer.accounts[acc_num].account_details.Balance-=amount
                msg="<td>Withdrawn Successfully!</td><br>"
            else:
                msg="<td>Not sufficient balance!</td><br>"
            
        else:
            msg="<p>Invalid account number</p><br>"
    return render(request, 'InfinityFinance/withdraw.html',{'customer':cur_customer, 'accounts':accounts,'msg':msg})

    #'customer':cur_customer, 'accounts':accounts

def deposit(request):
    accounts = cur_customer.accounts
    msg = ""
    if request.method == "POST":
        acc_num = int(request.POST.get('acc_no'))
        amount = int(request.POST.get('amount'))
        if acc_num in accounts:
            acc_q = Account_Data.objects.get(Accno=acc_num)
            balance = acc_q.Balance
            trans = Classes.Account(acc_q)
            trans.create_transaction(amount, "deposit")
            balance += amount
            acc_q.Balance = balance
            acc_q.save()
            cur_customer.accounts[acc_num].account_details.Balance += amount
            msg = "<td>Deposited Successfully!</td><br>"
        else:
            msg = "<p>Invalid account number</p><br>"
    return render(request, 'InfinityFinance/deposit.html', {'customer': cur_customer, 'accounts': accounts, 'msg': msg})


def stat_gen(request):
    accounts = cur_customer.accounts
    print(accounts)
    msg=""
    all_transactions = {}
    for acc in accounts:
        print("acc_no:",acc)
        acc_q=Account_Data.objects.get(Accno=int(acc))
        trans=Classes.Account(acc_q)
        #trans_rec=Transactions.objects.filter(Accno_id=int(acc))
        #print("trans_rec:",trans_rec)
        transaction=trans.get_transaction_log()
        trans_objs_list = list(transaction.values())
        all_transactions[acc] = all_transactions.get(acc, [])+trans_objs_list
        print("trans:",transaction)
    return render(request, 'InfinityFinance/stat_gen.html',{'customer':cur_customer, 'accounts':accounts, 'transaction':all_transactions,'msg':msg})

def get_transaction_action(request):
    accounts = cur_customer.accounts
    print("got:", request.GET)
    msg="filter"
    button_action = request.GET['account_action']
    all_transactions = {}
    if(button_action == 'withdraw'):
        for acc in accounts:
            transaction=Transactions.objects.filter(Accno_id=int(acc),Type="withdraw")
            print("withdraw:",transaction)
            all_transactions[acc] = list(transaction)
    elif(button_action == 'deposit'):
        for acc in accounts:
            transaction=Transactions.objects.filter(Accno_id=int(acc),Type="deposit")
            all_transactions[acc] = list(transaction)
    elif(button_action == 'all'):
        return redirect('InfinityFinance:stat_gen')
    #print("Account created successfully")
    print("all_trans:", all_transactions)
    return render(request,'InfinityFinance/stat_gen.html',{'customer':cur_customer, 'accounts':accounts, 'transaction':all_transactions,'msg':msg});

def get_function_chosen(request):
    print(request.GET) 
    #print("Got menu") 
    menu_chosen = request.GET['function_chosen']
    if(menu_chosen=='view_accounts'):
        return redirect('InfinityFinance:account_management') #name of view given in urls.py
    elif(menu_chosen=='withdraw'):
        return redirect('InfinityFinance:withdraw') #name of view given in urls.py
    elif(menu_chosen=='deposit'):
        return redirect('InfinityFinance:deposit') #name of view given in urls.py
    elif(menu_chosen=='stat_gen'):
        return redirect('InfinityFinance:stat_gen') #name of view given in urls.py
    elif(menu_chosen=='start_ecs'):
        return redirect('InfinityFinance:show_ecs_options')
    
def get_account_action(request):
    print("got:", request.GET)
    account_action = request.GET['account_action']
    #err_msg=""
    if(account_action == 'create'):
        cur_customer.create_account()
    elif(account_action == 'close'):
        print(request.GET)
        print("account:", cur_customer.accounts)
        close_accno = int(request.GET['close_accno'])
        #if(close_accno not in accounts):
        #    err_msg = "Invalid Account number!"
        #else:
        cur_customer.close_account(close_accno)
    else:
        print("Got neither create nor close")
    #print("Account created successfully")
    return redirect('InfinityFinance:account_management')

def show_ecs_options(request):
    return render(request, "InfinityFinance/ecs.html")
    
def redirect_ecs(request):
    ecs_option = request.GET['ecs_option']
    print("ecs_option", ecs_option)
    if(ecs_option == "new_ecs"):
        return redirect('InfinityFinance:start_ecs')
    if(ecs_option == 'view_ecs'):
        return redirect('InfinityFinance:show_due_bills')
        
def start_ecs(request):
    msg=""
    return render(request, 'InfinityFinance/set_up_ecs.html', {"msg":msg})
    
def store_new_ecs_data(request):
    #Make a class for ECS
    payer_name = request.GET['payer_name']
    upper_limit = request.GET['upper_limit']
    accno = int(request.GET['accno'])
    acc_obj = cur_customer.accounts[accno]
    ecs_obj = Classes.New_ECS(payer_name, acc_obj, upper_limit)
    msg = "New ECS Created Successfully!"
    return render(request, 'InfinityFinance/set_up_ecs.html', {"msg":msg})
    
def show_due_bills(request):
    accounts = cur_customer.accounts
    bills_list = []
    for acc_obj in accounts.values():
        ecs_list = ECS_Data.objects.filter(Account = acc_obj.account_details)
        for ecs in ecs_list:
            bills_for_cur_ecs = Bills.objects.filter(ECS_ID = ecs).filter(Completed = False)
            for bill in bills_for_cur_ecs:
                bill_details = [bill.id, ecs.Payer_Name, acc_obj.account_no, bill.Amount, ecs.Upper_Limit]
                if(bill.Amount<=ecs.Upper_Limit):
                    bill_details.append("yes")
                else:
                    bill_details.append("NO")
                #bills_list.extend(list(bills_for_cur_ecs))
                bills_list.append(bill_details)
    print(bills_list)
    return render(request, 'InfinityFinance/ecs_show_bills.html', {'bills_list':bills_list});
    
def pay_bill(request):
    bill_id = request.GET['bill_id']
    print("bill_id", bill_id)
    bill_obj = Bills.objects.get(id=bill_id)
    bill_obj.Completed = True
    bill_obj.save()
    return redirect('InfinityFinance:show_due_bills')
           
'''    
#Testing classes
def test_classes(request):
    print("got to test classes")
    login_obj = Classes.Login_Details('anj', 'anj123')
    cust_obj = Classes.Customer(login_obj)
    acc_obj = Classes.Account(1111)
    new_acc_obj = Classes.New_Account(111, cust_obj)
    new_cust_obj = Classes.New_Customer(login_obj, 'john', 'addr1', '100101')
'''