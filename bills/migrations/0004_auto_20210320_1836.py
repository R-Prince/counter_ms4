# Generated by Django 3.1.7 on 2021-03-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0003_auto_20210320_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_paid',
            field=models.BooleanField(default=False),
        ),
    ]
