from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import BillLineItem


@receiver(post_save, sender=BillLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update bill total on lineitem update/create
    """
    instance.bill.update_total()


@receiver(post_delete, sender=BillLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update bill total on lineitem delete
    """
    instance.bill.update_total()
