from django.contrib import admin
from .models import Customer, Account, Transactions, ECS_Data, Bills, Wallet

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('Cust_ID', 'Name', 'Phone_no', 'Email')

class AccountAdmin(admin.ModelAdmin):
    list_display = ('Account_number', 'Owner', 'Balance')

class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('Trans_ID', 'Account_number', 'Amount', 'Type')

'''class MoneyTransfersAdmin(admin.ModelAdmin):
    list_display = ('Trans_ID', 'From_Account_number', 'To_Account_number', 'Amount')
'''
class ECSDataAdmin(admin.ModelAdmin):
    list_display = ('ECS_ID', 'Payer_Name', 'Upper_Limit', 'Account')

class BillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'ECS_ID', 'Amount', 'Completed')

admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Transactions)
#admin.site.register(Money_Transfers)
admin.site.register(ECS_Data)
admin.site.register(Bills)
admin.site.register(Wallet)
