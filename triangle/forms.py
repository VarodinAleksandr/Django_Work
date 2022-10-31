from django import forms


class Triangle(forms.Form):
    catet_1 = forms.IntegerField(label='Catet_1', min_value=1)
    catet_2 = forms.IntegerField(label='Catet_2', min_value=1)
