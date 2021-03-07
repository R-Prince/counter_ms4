# Generated by Django 3.1.7 on 2021-03-07 17:53

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=75)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=50)),
                ('company_street_address1', models.CharField(max_length=80)),
                ('company_street_address2', models.CharField(blank=True, max_length=80)),
                ('company_city', models.CharField(max_length=40)),
                ('company_county', models.CharField(blank=True, max_length=80)),
                ('company_postcode', models.CharField(max_length=20)),
                ('company_logo', models.ImageField(blank=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]