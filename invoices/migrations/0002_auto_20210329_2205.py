# Generated by Django 3.1.7 on 2021-03-29 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='invoice_date',
            new_name='inv_date',
        ),
    ]