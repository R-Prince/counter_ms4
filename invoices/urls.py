from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_invoice, name='create_invoice'),
    path('invoices', views.invoices, name='invoices'),
    path(
        '<invoice_number>',
        views.edit_invoice, name='edit_invoice'),
    path(
        'delete_invoice/<invoice_number>',
        views.delete_invoice, name='delete_invoice'),
]
