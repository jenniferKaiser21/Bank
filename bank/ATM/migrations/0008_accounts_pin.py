# Generated by Django 4.1.7 on 2023-03-29 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATM', '0007_alter_transactions_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='pin',
            field=models.CharField(default='1234', max_length=4),
        ),
    ]
