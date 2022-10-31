from django.urls import path

from .views import calculate_triangle


app_name = 'triangle'
urlpatterns = [
    path('', calculate_triangle, name='calculation'),
]
