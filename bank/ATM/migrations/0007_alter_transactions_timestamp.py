# Generated by Django 4.1.7 on 2023-03-29 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATM', '0006_remove_transactions_success'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
