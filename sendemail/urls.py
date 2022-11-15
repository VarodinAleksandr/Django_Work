from django.urls import path

from .views import sender

app_name = 'sendemail'
urlpatterns = [
    path('', sender, name='sender'),
]
