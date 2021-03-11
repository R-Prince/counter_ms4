from django.urls import path
from . import views

urlpatterns = [
    path('', views.customers, name='customers'),
    path('create_customer/', views.create_customer, name='create_customer')
]
