# Generated by Django 5.0 on 2024-02-29 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0018_direct_buy_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direct_buy',
            name='size',
            field=models.CharField(default=5, max_length=50),
            preserve_default=False,
        ),
    ]
