# Generated by Django 4.1.7 on 2023-03-29 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATM', '0003_accounts_date_opened_accounts_last_updated_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accounts',
            options={'verbose_name': 'Account', 'verbose_name_plural': 'Accounts'},
        ),
        migrations.AlterModelOptions(
            name='transactions',
            options={'verbose_name': 'Transaction', 'verbose_name_plural': 'Transactions'},
        ),
        migrations.RenameField(
            model_name='accounts',
            old_name='current_amt',
            new_name='balance',
        ),
        migrations.AddField(
            model_name='transactions',
            name='ending_balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='transactions',
            name='starting_balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
