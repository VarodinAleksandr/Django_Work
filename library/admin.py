from django.contrib import admin

from .models import Author, Book, Publisher, Store


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    search_fields = ['name', 'age']
    list_filter = ['name', 'age']
    fields = ['name', 'age']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']
    fields = ['name']


class AuthorInline(admin.StackedInline):
    model = Author.books.through


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ['name', 'pages', 'price', 'rating', 'publisher', 'pubdate']
    search_fields = ['name', 'pages', 'price', 'rating', 'authors', 'publisher', 'pubdate']
    list_filter = ['name', 'pages', 'price', 'rating', 'authors', 'publisher', 'pubdate']
    fields = ['name', 'pages', 'price', 'rating', 'publisher', 'pubdate']
    raw_id_fields = ['publisher']
    inlines = [AuthorInline]


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'books']
    list_filter = ['name', 'books']
    fields = ['name', 'books']
    raw_id_fields = ['books']
