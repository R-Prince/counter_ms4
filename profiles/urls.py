from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_profile, name='create_profile'),
    path('', views.profile, name='profile'),
    path('profile_info', views.profile_info, name='profile_info'),
]
