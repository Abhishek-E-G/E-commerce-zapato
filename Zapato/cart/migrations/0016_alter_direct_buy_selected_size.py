# Generated by Django 5.0 on 2024-02-21 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0015_direct_buy_selected_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direct_buy',
            name='selected_size',
            field=models.CharField(choices=[('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=5, null=True),
        ),
    ]
