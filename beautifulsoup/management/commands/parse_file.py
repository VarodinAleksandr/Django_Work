from django.core.management.base import BaseCommand
from ...models import Author, Citaty


class Command(BaseCommand):

    def handle(self, *args, **options):
