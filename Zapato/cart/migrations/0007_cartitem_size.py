# Generated by Django 5.0 on 2024-02-19 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_remove_cartitem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='size',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
