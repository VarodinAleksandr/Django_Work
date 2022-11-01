from django import forms

from .models import Person


class Triangle(forms.Form):
    catet_1 = forms.IntegerField(label='Catet_1', min_value=1)
    catet_2 = forms.IntegerField(label='Catet_2', min_value=1)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
