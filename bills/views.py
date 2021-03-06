from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from .models import Bill, BillLineItem
from .forms import BillForm, BillLineForm
from django.contrib import messages
from customers.models import Customer
from django.contrib.auth.decorators import login_required


# Create Bill
@login_required
def create_bill(request):

    if request.method == 'POST':
        form_data = {
            'user': request.user,
            'customer_account': request.POST['customer_account'],
            'bill_date': request.POST['bill_date'],
            'due_date': request.POST['due_date'],
            'reference_number': request.POST['reference_number'],
            'bill_paid': request.POST.get('bill_paid', False)
        }
        # Use Form data to create Bill
        bill_form = BillForm(form_data)
        if bill_form.is_valid():
            bill = bill_form.save()
            key = []
            value = []
            # Create dict from request.POST data
            for data in request.POST.lists():
                key.append('bill')
                value.append(bill)
                key.append(data[0])
                value.append(data[1])
            data = zip(key, value)
            bill_line_data = (dict(data))

            # Remove unwanted POST data
            remove = (
                'csrfmiddlewaretoken', 'customer_account',
                'bill_date', 'due_date', 'reference_number')

            for items in remove:
                bill_line_data.pop(items)

            # Using dict create new Bill Line form
            for i in range(len(bill_line_data['description'])):
                for key, value in bill_line_data.items():
                    bill_line = {
                        'bill': bill_line_data['bill'],
                        'description': bill_line_data['description'][i],
                        'quantity': bill_line_data['quantity'][i],
                        'price': bill_line_data['price'][i],
                        'item_tax': bill_line_data['tax'][i],
                    }
                bill_line_form = BillLineForm(bill_line)
                bill_line_form.save()
            messages.success(request, ("Bill Successfully Created!"))
            return redirect(reverse('profile'))
        else:
            messages.error(request, (
                "There was an error with your form, please try again"))
            return redirect(reverse('create_bill'))

    bill_form = BillForm()
    customers = Customer.objects.filter(user=request.user)
    context = {
        'bill_form': bill_form,
        'customers': customers
    }

    template = 'bills/create_bill.html'

    return render(request, template, context)


@login_required
def bills(request):
    # View users bills
    bills = Bill.objects.filter(user=request.user)
    template = 'bills/bills.html'
    context = {
        'bills': bills
    }
    return render(request, template, context)


@login_required
def edit_bill(request, bill_number):
    # Edit Bill
    bill = Bill.objects.get(bill_number=bill_number)
    billLines = BillLineItem.objects.filter(bill=bill)

    if request.method == "POST":
        form_data = {
            'user': request.user,
            'customer_account': request.POST['customer_account'],
            'bill_date': request.POST['bill_date'],
            'due_date': request.POST['due_date'],
            'reference_number': request.POST['reference_number'],
            'bill_paid': request.POST.get('bill_paid', False)
        }
        bill_form = BillForm(form_data, instance=bill)
        if bill_form.is_valid():
            bill_form.save()
            messages.success(request, ("Bill Successfully Updated!"))
            return redirect(reverse('profile'))

    customers = Customer.objects.filter(user=request.user)
    form = BillForm(instance=bill)

    template = 'bills/edit_bill.html'
    context = {
        'bill': bill,
        'billLines': billLines,
        'customers': customers,
        'form': form
    }

    return render(request, template, context)


@login_required
def delete_bill(request, bill_number):
    # Delete Bill
    bill = get_object_or_404(Bill, bill_number=bill_number)
    bill.delete()
    messages.success(request, ("Bill Successfully Deleted!"))

    return redirect(reverse('profile'))
