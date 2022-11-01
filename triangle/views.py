import math

from django.shortcuts import get_object_or_404, redirect, render

from .forms import PersonForm, Triangle
from .models import Person


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


def person(request):
    form = PersonForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            obj = Person.objects.create(**form.cleaned_data)
            return redirect('triangle:update_person', obj.id)
    elif request.method == 'GET':
        context = {
            "form": form
        }
        return render(request, 'triangle/create_person.html', context)


def update_person(request, pk):
    user = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=user)
        if form.is_valid():
            obj = form.save()
            return redirect('triangle:update_person', obj.id)
    elif request.method == 'GET':
        form = PersonForm(instance=user)
    return render(request, 'triangle/person.html', {"form": form, 'obj': user})
