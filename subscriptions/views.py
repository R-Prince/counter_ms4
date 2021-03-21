from django.shortcuts import render, get_object_or_404
from .models import Subscription
from profiles.models import UserProfile
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta


# Update Users Subscription
@login_required
def update_subscription(request):

    current_subscription = get_object_or_404(Subscription, user=request.user)
    profile = get_object_or_404(UserProfile, user=request.user)
    sub_end = date.today() + timedelta(days=31)

    context = {
        'current_subscription': current_subscription,
        'profile': profile,
        'sub_end': sub_end,
        'stripe_public_key': 'pk_test_51IXY2lAeZyzq5JP9qRM2UnKZnKMGIbrb5z5XeTBPRkx6sKyxFFxvtmfmKhbB7Y0uAoPUlylpF0AUP4uVmPg33SI90047fwc770',
        'client_secret': 'test secret key'
    }
    template = 'subscription/update_subscription.html'
    return render(request, template, context)
