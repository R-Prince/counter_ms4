from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """ User Profile """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=75, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    company_name = models.CharField(max_length=50, null=False, blank=False)
    company_street_address1 = models.CharField(
        max_length=80, null=False, blank=False)
    company_street_address2 = models.CharField(
        max_length=80, blank=True)
    company_city = models.CharField(max_length=40, null=False, blank=False)
    company_county = models.CharField(max_length=80, blank=True)
    company_postcode = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.company_name
