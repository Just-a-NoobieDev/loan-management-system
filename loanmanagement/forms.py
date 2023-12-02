from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    pass

    class Meta:
        model = Person
        fields = ('name', 'address', 'picture', 'document')
