# Generated by Django 5.0 on 2024-02-19 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_direct_buy_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='size',
        ),
        migrations.RemoveField(
            model_name='direct_buy',
            name='size',
        ),
    ]
