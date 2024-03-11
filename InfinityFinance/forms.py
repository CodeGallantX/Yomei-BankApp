from django import forms

class TransferForm(forms.Form):
    recipient_account = forms.CharField(max_length=100)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

class DepositForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

class WithdrawForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)