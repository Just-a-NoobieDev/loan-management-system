# app/forms.py
from django import forms

from loanmanagement.models import Collector


# class PaymentForm(forms.ModelForm):
#     class Meta:
#         model = Payment
#         fields = ['name', 'balance', 'amount', 'or_number', 'new_balance']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Collector
        fields = '__all__'
