from django.db import models
from django.contrib.auth.models import User


# User Subscription
class Subscription(models.Model):
    user = user = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return f'{self.user} subscription will end on: {self.end_date}'
