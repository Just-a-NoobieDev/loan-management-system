from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'address', 'picture', 'document')


class UserRegistration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
