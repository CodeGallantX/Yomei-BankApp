from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class AccountDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add fields for account details, such as first name, last name, email, etc.
    # Example:
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.user.username
