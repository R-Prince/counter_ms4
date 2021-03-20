from django.db import models
import uuid
from django.db.models import Sum
from django.contrib.auth.models import User


# User Bills
class Bill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bill_number = models.CharField(max_length=32, null=False, editable=False)
    customer_account = models.CharField(
        max_length=200, null=False, blank=False)
    bill_date = models.DateField(null=False, blank=False)
    due_date = models.DateField(null=False, blank=False)
    reference_number = models.CharField(max_length=50, null=False, blank=False)
    bill_paid = models.BooleanField(default=False)
    bill_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_bill_number(self):
        """
        Generate a random, unique bill number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update bill total each time a bill line item is added
        """
        self.bill_total = self.lineitems.aggregate(
            Sum('item_total'))['item_total__sum']
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the bill number
        if it hasn't been set already.
        """
        if not self.bill_number:
            self.bill_number = self._generate_bill_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.bill_number


# Bill Line items
class BillLineItem(models.Model):
    bill = models.ForeignKey(
        Bill, null=False, blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems')
    description = models.CharField(max_length=400, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False)
    item_tax = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False)
    item_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False,
        editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the item_total
        """
        item_subtotal = self.price * self.quantity
        self.item_total = item_subtotal + self.item_tax
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description
