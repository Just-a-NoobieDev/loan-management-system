from django import forms

from loanmanagement.models import Person


class LoginForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'