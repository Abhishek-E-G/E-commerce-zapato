# Generated by Django 5.0 on 2023-12-29 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=20)),
                ('email1', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=20)),
            ],
        ),
    ]
