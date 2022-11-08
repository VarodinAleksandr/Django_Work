import random
from datetime import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker

from ...models import Author, Book, Publisher, Store


class Command(BaseCommand):

    def handle(self, *args, **options):
        fake = Faker()
        number_users = 20
        user_bulk = []
        publisher_bulk = []
        authors_bulk = []
        for i in range(number_users):
            age = random.randint(20, 80)
            name = fake.name()
            full_name_list = name.split()
            first_name = full_name_list[0]
            last_name = full_name_list[1]
            username = f'{first_name[0].lower()}{last_name.lower()}'
            email = f'{username}@example.com'
            password = fake.password()
            user_bulk.append(User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password))
            publisher_bulk.append(Publisher(name=name))
            authors_bulk.append(Author(name=name, age=age))
        User.objects.bulk_create(user_bulk)
        Publisher.objects.bulk_create(publisher_bulk)
        Author.objects.bulk_create(authors_bulk)

        counter = 0
        authors_ids = [i.id for i in Author.objects.all()]
        for publisher in Publisher.objects.all():
            for i in range(20):
                counter = counter + 1
                book = Book.objects.create(
                    name=f"Book{counter}",
                    pages=random.randint(300, 1000),
                    price=random.randint(50, 300),
                    rating=random.uniform(0.1, 10.0),
                    publisher=publisher,
                    pubdate=datetime.now().date()
                )
                book.authors.add(*random.choices(authors_ids, k=3))

        books = list(Book.objects.all())
        for i in range(10):
            temp_books = [books.pop(0) for i in range(10)]
            store = Store.objects.create(name=f"Store{i+1}")
            store.books.set(temp_books)
            store.save()
