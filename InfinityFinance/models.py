from django.db import models
from django.contrib.auth.models import User

'''

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Personal Information
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    id_number = models.CharField(max_length=50, null=True, blank=True)
    # Financial Information
    account_number = models.CharField(max_length=20, unique=True)
    ACCOUNT_TYPES = [
        ('savings', 'Savings Account'),
        ('current', 'Current Account'),
    ]
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    is_active = models.BooleanField(default=True)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # Security Information
    security_questions = models.TextField(null=True, blank=True)
    two_factor_auth_enabled = models.BooleanField(default=False)
    # Preferences
    language_preference = models.CharField(max_length=20, default='en')
    currency_preference = models.CharField(max_length=3, default='USD')
    notification_settings = models.BooleanField(default=True)
    # Additional Details
    subscription_status = models.BooleanField(default=False)
    membership_level = models.CharField(max_length=50, null=True, blank=True)
    plan_details = models.TextField(null=True, blank=True)
    account_creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class UserBankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    ACCOUNT_TYPES = [
        ('savings', 'Savings Account'),
        ('current', 'Current Account'),
    ]
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    is_active = models.BooleanField(default=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # Add other fields as needed

    def __str__(self):
        return f"{self.user.username}'s Bank Account"





class Bill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    is_paid = models.BooleanField(default=False)

class AirtimePurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    is_successful = models.BooleanField(default=False)
    

'''

# Create your models here.
class Customer(models.Model):
    Cust_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Phone_no = models.CharField(max_length=10)
    #Fixed length can't be specified. Only max_length can be.
    Email = models.EmailField()
    #Username = models.CharField(max_length=30)
    #Password = models.CharField(max_length=30)
    class Meta:
        db_table = 'customer'
   
class Account(models.Model):
    Account_number = models.IntegerField(primary_key=True)
    Owner = models.ForeignKey( Customer, on_delete=models.CASCADE)
    Balance = models.FloatField()
    #Name = models.CharField(max_length=200)
    class Meta:
        db_table = 'account'

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=10, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=500)

    def __str__(self):
        return f"{self.user.username}'s Wallet"


'''    
class Deposits(models.Model): 
    Trans_ID = models.AutoField(primary_key=True)
    Account_number = models.ForeignKey(Account, on_delete=models.CASCADE)
    Amount = models.FloatField()
    class Meta:
        db_table = 'deposits'
        
class Withdraws(models.Model): 
    Trans_ID = models.AutoField(primary_key=True)
    Account_number = models.ForeignKey(Account, on_delete=models.CASCADE)
    Amount = models.FloatField()
    class Meta:
        db_table = 'withdraws' 
'''

class Transactions(models.Model): 
    Trans_ID = models.AutoField(primary_key=True)
    Account_number = models.ForeignKey( Account, on_delete=models.CASCADE)
    Amount = models.FloatField()
    Type = models.CharField(max_length=30)
    #Type can be "withdraw" or "deposit"
    class Meta:
        db_table = 'transactions'
        
def Money_Transfers(self, Trans_ID, From_accno, To_accno, Amount):             
    Trans_ID = models.AutoField(primary_key=True)
    From_accno = models.ForeignKey( Account, on_delete=models.CASCADE, related_name = 'From_accno')
    To_accno = models.ForeignKey( Account, on_delete=models.CASCADE, related_name = 'To_accno')
    Amount = models.FloatField()

    class Meta:
        db_table = 'transfers'
    
    
        

    
class Bills(models.Model):
    #id column created implicitly
    Amount = models.FloatField()
    Completed = models.BooleanField()
    class Meta:
        db_table = 'bills'        
    