from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages
from subscriptions.models import Subscription
from bills.models import Bill
from invoices.models import Invoice
from datetime import date, timedelta


@login_required(login_url='/accounts/confirm-email/')
def create_profile(request):
    # Create user profile and subscription
    if request.method == 'POST':

        form_data = {
            'user': request.user,
            'full_name': request.POST['full_name'],
            'email': request.user.email,
            'phone_number': request.POST['phone_number'],
            'company_name': request.POST['company_name'],
            'company_street_address1': request.POST['company_street_address1'],
            'company_street_address2': request.POST['company_street_address2'],
            'company_city': request.POST['company_city'],
            'company_county': request.POST['company_county'],
            'company_postcode': request.POST['company_postcode'],
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
            messages.info(request, 'Profile created Successfully')

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
        messages.info(request, 'Please create a Profile')
        return redirect(reverse('create_profile'))

    user_subscription = get_object_or_404(Subscription, user=request.user)
    bills = Bill.objects.filter(user=request.user)[:4]
    invoices = Invoice.objects.filter(user=request.user)[:4]
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'bills': bills,
        'invoices': invoices,
    }
    # check if user subscription is valid
    if user_subscription.end_date < date.today():
        messages.success(request, 'Please udpate subscription')
        return redirect(reverse('update_sub'))
    else:
        return render(request, template, context)


@login_required
def profile_info(request):
    # View and Update User Profile
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)

    template = 'profiles/profile_info.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

