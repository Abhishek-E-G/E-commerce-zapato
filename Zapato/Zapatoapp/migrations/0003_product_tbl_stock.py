# Generated by Django 5.0 on 2024-01-31 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zapatoapp', '0002_product_tbl'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_tbl',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]