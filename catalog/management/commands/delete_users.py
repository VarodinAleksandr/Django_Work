from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Delete users'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        users_ids = kwargs['user_id']
        superusers = User.objects.filter(is_superuser=True)
        for i in superusers:
            if i.id in users_ids:
                raise Exception('This is SUPERUSER, cannot be deleted')
        users_to_delete = User.objects.filter(id__in=users_ids)
        users_to_delete.delete()
