from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help = 'Generate random users'

    def add_arguments(self, parser):
        parser.add_argument('number_users', type=int, choices=range(2, 11),
                            help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        fake = Faker()
        number_users = kwargs['number_users']
        bulk = []
        for i in range(number_users):
            name = fake.name()
            full_name_list = name.split()
            first_name = full_name_list[0]
            last_name = full_name_list[1]
            username = f'{first_name[0].lower()}{last_name.lower()}'
            email = f'{username}@example.com'
            password = fake.password()
            bulk.append(User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password))
        User.objects.bulk_create(bulk)
