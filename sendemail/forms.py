from django import forms
from django.utils import timezone


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)


class CeleryForm(forms.Form):
    email = forms.EmailField(max_length=254)
    text_remainder = forms.CharField(max_length=254)
    date = forms.DateTimeField(widget=DateTimeInput())

    def clean_date(self):
        value = self.cleaned_data['date']
        now = timezone.now()
        maximum = now + timezone.timedelta(days=2)
        if now >= value or value >= maximum:
            self.add_error('date', 'Wrong date')
        return value
