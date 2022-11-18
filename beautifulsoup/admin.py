from django.contrib import admin

from .models import Author, Citaty


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    fields = ['name']


@admin.register(Citaty)
class CitatyAdmin(admin.ModelAdmin):
    list_display = ['text', 'author']
