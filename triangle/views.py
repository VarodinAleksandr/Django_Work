import math

from django.shortcuts import render

from .forms import Triangle


def calculate_triangle(request):
    form = Triangle(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            a = form.cleaned_data["catet_1"]
            b = form.cleaned_data["catet_2"]
            c = (a ** 2) + (b ** 2)
            result = math.sqrt(c)
            context = {"result": result}
            return render(request, 'triangle/result.html', context)
    context = {
        "form": form
    }
    return render(request, 'triangle/createform.html', context)
