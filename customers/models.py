from django.db import models
from profiles.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Customer(models.Model):
    """ User Customers """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=75, null=False, blank=False)
    customer_email = models.EmailField(max_length=254, null=False, blank=False)
    customer_phone_number = models.CharField(
        max_length=20, null=False, blank=False)
    company_name = models.CharField(max_length=254, null=False, blank=False)
    company_street_address1 = models.CharField(
        max_length=80, null=False, blank=False)
    company_street_address2 = models.CharField(
        max_length=80, blank=True)
    company_city = models.CharField(max_length=40, null=False, blank=False)
    company_county = models.CharField(max_length=80, blank=True)
    company_postcode = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.company_name
