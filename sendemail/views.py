from django.http import HttpResponse
from django.shortcuts import render

from .forms import CeleryForm
from .task import add_sendmail


def sender(request):
    form = CeleryForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data['email']
            text_remainder = form.cleaned_data['text_remainder']
            date = form.cleaned_data['date']
            add_sendmail.apply_async(args=(email, text_remainder), eta=date)
            context = {
                "form": form
            }
            return render(request, 'sendemail/mail_detail.html', context)
        else:
            return HttpResponse(form.errors['date'].as_data())
    if request.method == 'GET':
        context = {
            "form": form
        }
        return render(request, 'sendemail/sendemail.html', context)
