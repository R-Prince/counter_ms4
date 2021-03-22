from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages
from subscriptions.models import Subscription
from datetime import date, timedelta


@login_required(login_url='/accounts/confirm-email/')
def create_profile(request):
    # Create user profile and subscription
    if request.method == 'POST':

        form_data = {
            'user': request.user,
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'company_name': request.POST['company_name'],
            'company_street_address1': request.POST['company_street_address1'],
            'company_street_address2': request.POST['company_street_address2'],
            'company_city': request.POST['company_city'],
            'company_county': request.POST['company_county'],
            'company_postcode': request.POST['company_postcode'],
            'company_logo': request.POST['company_logo']
        }
        user_profile_form = UserProfileForm(form_data)
        if user_profile_form.is_valid():
            user_profile_form.save()
            # Create 14 day free Subscription
            end_date = date.today() + timedelta(days=14)
            create_subscription = Subscription(
                user=request.user,
                start_date=date.today(),
                end_date=end_date)
            create_subscription.save()

        return redirect(reverse('profile'))

    user_profile_form = UserProfileForm()
    template = 'profiles/create_profile.html'
    context = {
        'user_profile_form': user_profile_form,
    }
    return render(request, template, context)


@login_required
def profile(request):
    try:
        profile = get_object_or_404(UserProfile, user=request.user)
    except Exception:
        messages.success(request, 'Please create a profile first')
        return redirect(reverse('create_profile'))

    user_subscription = get_object_or_404(Subscription, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }
    # check if user subscription is valid
    if user_subscription.end_date < date.today():
        messages.success(request, 'Please udpate subscription')
        return redirect(reverse('update_sub'))
    else:
        return render(request, template, context)
