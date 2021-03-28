from django.shortcuts import render, get_list_or_404, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import CustomerForm
from django.contrib import messages


@login_required
def customers(request):
    # View users customers
    customers = Customer.objects.filter(user=request.user)
    template = 'customers/customers.html'
    context = {
        'customers': customers
    }
    return render(request, template, context)


@login_required
def create_customer(request):
    # Create user customer
    if request.method == 'POST':

        form_data = {
            'user': request.user,
            'customer_name': request.POST['customer_name'],
            'customer_email': request.POST['customer_email'],
            'customer_phone_number': request.POST['customer_phone_number'],
            'company_name': request.POST['company_name'],
            'company_street_address1': request.POST['company_street_address1'],
            'company_street_address2': request.POST['company_street_address2'],
            'company_city': request.POST['company_city'],
            'company_county': request.POST['company_county'],
            'company_postcode': request.POST['company_postcode'],
        }
        customer_form = CustomerForm(form_data)
        if customer_form.is_valid():
            customer_form.save()
            messages.success(
                request, 'Successfully created Customer')

        return redirect(reverse('customers'))

    customer_form = CustomerForm()
    template = 'customers/create_customer.html'
    context = {
        'customer_form': customer_form,
    }
    return render(request, template, context)


@login_required
def edit_customer(request, customer_id):
    # Edit Customer Details
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer updated successfully')

    form = CustomerForm(instance=customer)

    template = 'customers/edit_customer.html'
    context = {
        'form': form,
        'customer': customer
    }

    return render(request, template, context)
