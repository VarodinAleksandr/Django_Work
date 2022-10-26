# Generated by Django 4.1.2 on 2022-10-26 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_rename_cars_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.client'),
        ),
    ]
