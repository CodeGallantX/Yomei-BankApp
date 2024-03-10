from django.contrib import admin
from django.urls import path
from .models import Account, Transaction

# Register your models here

admin.site.register(Account)
admin.site.register(Transaction)