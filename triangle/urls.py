from django.urls import path

from .views import calculate_triangle, person, update_person

app_name = 'triangle'
urlpatterns = [
    path('', calculate_triangle, name='calculation'),
    path('person', person, name='person'),
    path('person/<int:pk>', update_person, name='update_person'),
]
