from django.shortcuts import render, redirect, reverse
from .forms import BillForm, BillLineForm
from django.contrib import messages


# Create Bill
def create_bill(request):
    if request.method == 'POST':
        form_data = {
            'user': request.user,
            'customer_account': request.POST['customer_account'],
            'bill_date': request.POST['bill_date'],
            'due_date': request.POST['due_date'],
            'reference_number': request.POST['reference_number'],
            'bill_paid': request.POST['bill_paid'],
        }
        bill_form = BillForm(form_data)
        if bill_form.is_valid():
            bill = bill_form.save()
            bill_line_data = {
                'bill': bill,
                'description': request.POST['description'],
                'quantity': request.POST['quantity'],
                'price': request.POST['price'],
                'item_tax': request.POST['item_tax'],
            }
            bill_line_form = BillLineForm(bill_line_data)
            if bill_line_form.is_valid():
                bill_line_form.save()
                messages.success(request, ("Bill Successfully Created!"))
                return redirect(reverse('profile'))

    bill_form = BillForm()
    bill_line_form = BillLineForm()

    context = {
        'bill_form': bill_form,
        'bill_line_form': bill_line_form
    }

    template = 'bills/create_bill.html'

    return render(request, template, context)
