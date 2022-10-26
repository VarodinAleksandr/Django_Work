from django.db import models
from django.contrib.auth.models import User


class Manager(models.Model):
    user = models.ForeignKey(User, related_name='managers', on_delete=models.CASCADE)
    position = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.user.get_full_name()}, {self.position}'


class Car(models.Model):
    BMW = 'bmw'
    FORD = 'ford'
    TOYOTA = 'toyota'
    EMPTY = ''
    CAR_BRANDS_CHOICES = [(BMW, 'bmw'),
                          (FORD, 'ford'),
                          (TOYOTA, 'toyota'),
                          (EMPTY, '')
                          ]
    BLACK = 'black'
    WHITE = 'white'
    DEFAULT = ''
    CAR_COLOUR_CHOICES = [(BLACK, 'black'),
                          (WHITE, 'white'),
                          (DEFAULT, '')]
    car_brands = models.CharField(max_length=25, choices=CAR_BRANDS_CHOICES, default=EMPTY)
    car_colour = models.CharField(max_length=25, choices=CAR_COLOUR_CHOICES, default=DEFAULT)
    vin_code = models.CharField(max_length=100)
    managers = models.ManyToManyField(Manager)
    owner = models.OneToOneField('Client', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.car_colour}, {self.car_brands}, owned by {self.owner.user.get_full_name()}'


class Client(models.Model):
    TELEGRAM = 'telegram'
    VIBER = 'viber'
    CALL = 'call'
    MESSENGER_CHOICES = [(TELEGRAM, 'telegram'),
                         (VIBER, 'viber'),
                         (CALL, 'call'),
                         ]
    comment = models.TextField(null=True, blank=True)
    messenger = models.CharField(max_length=25, choices=MESSENGER_CHOICES, default=CALL)
    user = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, related_name='clients', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.get_full_name()}, {self.messenger}'
