from django.shortcuts import render
from .forms import BillForm, BillLineForm


# Create Bill
def create_bill(request):
    bill_form = BillForm()
    bill_line_form = BillLineForm()

    context = {
        'bill_form': bill_form,
        'bill_line_form': bill_line_form
    }

    template = 'bills/create_bill.html'

    return render(request, template, context)
