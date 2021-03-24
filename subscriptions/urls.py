from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('update_sub', views.update_subscription, name='update_sub'),
    path(
        'checkout_success/',
        views.checkout_success, name='checkout_success'),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data,
        name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
