from django.urls import path
from . import views

urlpatterns = [
    path('update_sub', views.update_subscription, name='update_sub'),
]