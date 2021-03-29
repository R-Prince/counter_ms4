from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_bill, name='create_bill'),
    path('bills', views.bills, name='bills'),
    path(
        '<bill_number>',
        views.edit_bill, name='edit_bill'),
]
