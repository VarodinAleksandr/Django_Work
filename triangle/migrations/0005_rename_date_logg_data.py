# Generated by Django 4.1.2 on 2022-11-04 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('triangle', '0004_alter_logg_method'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logg',
            old_name='date',
            new_name='data',
        ),
    ]
