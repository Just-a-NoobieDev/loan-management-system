from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Person, Loan, Payment


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'address', 'picture', 'document')


class UserRegistration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['client_id', 'loan_date', 'duration_period', 'interest_rate', 'loan_amount', 'loan_maturity', 'guarantor', 'processing_fee', 'loan_balance', 'net', 'checking_no']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client_id'].widget = forms.Select()
        self.fields['client_id'].queryset = Person.objects.all()
        self.fields['loan_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['duration_period'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['loan_maturity'].widget = forms.DateInput(attrs={'type': 'date'})
        
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['loan_id', 'amount', 'payment_date', 'or_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['loan_id'].widget = forms.Select()
        self.fields['loan_id'].queryset = Loan.objects.all()
        self.fields['payment_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})