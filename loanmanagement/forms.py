from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Person, Collector, Loan, Payment


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class UserRegistration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']        


class CollectorForm(forms.ModelForm):
    class Meta:
        model = Collector
        fields = ('name',)

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['client_id', 'loan_date', 'duration_period', 'interest_rate', 'loan_amount', 'loan_maturity', 'guarantor', 'processing_fee', 'loan_balance', 'net', 'checking_no', 'has_active_loan']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client_id'].widget = forms.Select()
        self.fields['client_id'].queryset = Person.objects.all()
        self.fields['loan_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['duration_period'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['loan_maturity'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['has_active_loan'].widget = forms.CheckboxInput(attrs={'type': 'checkbox'})
        
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['loan_id', 'amount', 'payment_date', 'or_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['loan_id'].widget = forms.Select()
        self.fields['loan_id'].queryset = Loan.objects.all()
        self.fields['payment_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['loan_id'].queryset = self.fields['loan_id'].queryset.filter(has_active_loan=True)