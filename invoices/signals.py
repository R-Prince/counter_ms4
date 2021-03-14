from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import InvoiceItem


@receiver(post_save, sender=InvoiceItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update invoice total on invoiceitem update/create
    """
    instance.invoice.update_total()


@receiver(post_delete, sender=InvoiceItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update invoice total on invoiceitem delete
    """
    instance.invoice.update_total()
