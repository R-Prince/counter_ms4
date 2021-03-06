# Generated by Django 3.1.7 on 2021-03-30 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.CharField(editable=False, max_length=32)),
                ('customer_account', models.CharField(max_length=200)),
                ('bill_date', models.DateField()),
                ('due_date', models.DateField()),
                ('reference_number', models.CharField(max_length=50)),
                ('bill_paid', models.BooleanField(default=False)),
                ('bill_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BillLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=400)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('item_tax', models.DecimalField(decimal_places=2, max_digits=6)),
                ('item_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='bills.bill')),
            ],
        ),
    ]
