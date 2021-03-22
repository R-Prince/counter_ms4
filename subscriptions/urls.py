from django.urls import path
from . import views

urlpatterns = [
    path('update_sub', views.update_subscription, name='update_sub'),
    path(
        'checkout_success/',
        views.checkout_success, name='checkout_success'),
]
