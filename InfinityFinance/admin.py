from django.contrib import admin
from django.urls import path
from .models import Customer, Account, Transactions, Money_Transfers, ECS_Data, Bills


# Register your models here

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('Cust_ID', 'Name', 'Phone_no', 'Email')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('Accno', 'Owner', 'Balance')

@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('Trans_ID', 'Accno', 'Amount', 'Type')

@admin.register(Money_Transfers)
class MoneyTransfersAdmin(admin.ModelAdmin):
    list_display = ('Trans_ID', 'From_accno', 'To_accno', 'Amount')

@admin.register(ECS_Data)
class ECSDataAdmin(admin.ModelAdmin):
    list_display = ('ECS_ID', 'Payer_Name', 'Upper_Limit', 'Account')

@admin.register(Bills)
class BillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'ECS_ID', 'Amount', 'Completed')

