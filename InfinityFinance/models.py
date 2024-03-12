from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



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


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Transaction(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, default=None)  # Example default value

    def __str__(self):
        return self.description

from django.db import models
from .models import Account

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description



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
    

