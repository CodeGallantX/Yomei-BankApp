from django.contrib import admin
from .models import Customer, Account, Transactions, Money_Transfers, ECS_Data, Bills

# Register models here
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('Cust_ID', 'Name', 'Phone_no', 'Email')
admin.site.register(Customer, CustomerAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('Accno', 'Owner', 'Balance')
admin.site.register(Account, AccountAdmin)

class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('Trans_ID', 'Accno', 'Amount', 'Type')
admin.site.register(Transactions, TransactionsAdmin)

class MoneyTransfersAdmin(admin.ModelAdmin):
    list_display = ('Trans_ID', 'From_accno', 'To_accno', 'Amount')
admin.site.register(Money_Transfers, MoneyTransfersAdmin)

class ECSDataAdmin(admin.ModelAdmin):
    list_display = ('ECS_ID', 'Payer_Name', 'Upper_Limit', 'Account')
admin.site.register(ECS_Data, ECSDataAdmin)

class BillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'ECS_ID', 'Amount', 'Completed')
admin.site.register(Bills, BillsAdmin)
