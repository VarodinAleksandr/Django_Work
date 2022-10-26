# Generated by Django 4.1.2 on 2022-10-26 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('messenger', models.CharField(choices=[('telegram', 'telegram'), ('viber', 'viber'), ('call', 'call')], default='call', max_length=25)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='catalog.manager')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('car_brands', models.CharField(choices=[('bmw', 'bmw'), ('ford', 'ford'), ('toyota', 'toyota'), ('', '')], default='', max_length=25)),
                ('car_colour', models.CharField(choices=[('black', 'black'), ('white', 'white'), ('', '')], default='', max_length=25)),
                ('vin_code', models.CharField(max_length=100)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='catalog.client')),
                ('managers', models.ManyToManyField(to='catalog.manager')),
            ],
        ),
    ]