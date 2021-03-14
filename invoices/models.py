from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Invoice(models.Model):
    """ User Invoices """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(null=False, blank=False)
    due_date = models.DateField(null=False, blank=False)
    invoice_number = models.CharField(max_length=20, null=False, blank=False)
    customer_account = models.CharField(
        max_length=200, null=False, blank=False)
    invoice_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False,
        default=0)

    def update_total(self):
        """ Update Invoice Total """
        self.invoice_total = self.lineitems.aggregate(
            Sum('item_total'))['lineitem_total_sum']
        self.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_number


class InvoiceItem(models.Model):
    """ Invoice Items """
    invoice_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, null=False, blank=False)
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


class InvoiceStatus(models.Model):
    invoice_id = models.OneToOneField(Invoice, on_delete=models.CASCADE)
    paid = models.BooleanField()
    date_paid = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.paid
