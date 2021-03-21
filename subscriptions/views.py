from django.shortcuts import render, get_object_or_404
from .models import Subscription
from profiles.models import UserProfile
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from django.conf import settings
import stripe


# Update Users Subscription
@login_required
def update_subscription(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    current_subscription = get_object_or_404(Subscription, user=request.user)
    profile = get_object_or_404(UserProfile, user=request.user)
    sub_end = date.today() + timedelta(days=31)
    current_sub_price = 1999

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=current_sub_price,
        currency=settings.STRIPE_CURRENCY,
    )

    context = {
        'current_subscription': current_subscription,
        'profile': profile,
        'sub_end': sub_end,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }
    template = 'subscription/update_subscription.html'
    return render(request, template, context)
