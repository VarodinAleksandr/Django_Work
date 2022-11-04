from django.contrib import admin

from .models import Logg


@admin.register(Logg)
class LoggAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'method', 'path']
    search_fields = ['method', 'path', 'data']
    list_filter = ['timestamp', 'method']
