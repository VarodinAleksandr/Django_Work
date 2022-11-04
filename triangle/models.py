from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Logg(models.Model):
    POST = 'POST'
    GET = 'GET'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
    CHOISES = [(POST, 'post'),
               (GET, 'get'),
               (PUT, 'put'),
               (PATCH, 'patch'),
               (DELETE, 'delete'),
               ]
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=35, choices=CHOISES, default=POST)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.JSONField(default=dict)

    def __str__(self):
        return f'{self.timestamp} {self.method} {self.path}'
