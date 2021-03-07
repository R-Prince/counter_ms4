from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm


@login_required(login_url='/accounts/confirm-email/')
def create_profile(request):
    # Create user profile
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

    user_profile_form = UserProfileForm()
    template = 'profiles/create_profile.html'
    context = {
        'user_profile_form': user_profile_form,
    }
    return render(request, template, context)
