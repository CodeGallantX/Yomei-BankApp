from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class TransactionType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TransactionCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TransactionStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE)
    status = models.ForeignKey(TransactionStatus, on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.timestamp}"
