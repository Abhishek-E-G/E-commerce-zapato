# Generated by Django 5.0 on 2024-02-19 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_cartitem_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='size',
        ),
    ]
