from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from .models import Invoice, InvoiceLineItem
from .forms import InvoiceForm, InvoiceLineForm
from django.contrib import messages
from customers.models import Customer
from django.contrib.auth.decorators import login_required


# Create Invoice
@login_required
def create_invoice(request):

    if request.method == 'POST':
        form_data = {
            'user': request.user,
            'customer_account': request.POST['customer_account'],
            'invoice_date': request.POST['invoice_date'],
            'due_date': request.POST['due_date'],
            'reference_number': request.POST['reference_number'],
            'invoice_paid': request.POST.get('invoice_paid', False)
        }
        # Use Form data to create Invoice
        invoice_form = InvoiceForm(form_data)
        if invoice_form.is_valid():
            invoice = invoice_form.save()
            key = []
            value = []
            # Create dict from request.POST data
            for data in request.POST.lists():
                key.append('invoice')
                value.append(invoice)
                key.append(data[0])
                value.append(data[1])
            data = zip(key, value)
            invoice_line_data = (dict(data))

            # Remove unwanted POST data
            remove = (
                'csrfmiddlewaretoken', 'customer_account',
                'invoice_date', 'due_date', 'reference_number')

            for items in remove:
                invoice_line_data.pop(items)

            # Using dict create new Invoice Line form
            for i in range(len(invoice_line_data['description'])):
                for key, value in invoice_line_data.items():
                    invoice_line = {
                        'invoice': invoice_line_data['invoice'],
                        'description': invoice_line_data['description'][i],
                        'quantity': invoice_line_data['quantity'][i],
                        'price': invoice_line_data['price'][i],
                        'item_tax': invoice_line_data['tax'][i],
                    }
                invoice_line_form = InvoiceLineForm(invoice_line)
                invoice_line_form.save()
            messages.success(request, ("Invoice Successfully Created!"))
            return redirect(reverse('profile'))
        else:
            messages.error(request, (
                "There was an error with your form, please try again"))
            return redirect(reverse('create_invoice'))

    invoice_form = InvoiceForm()
    customers = Customer.objects.filter(user=request.user)
    context = {
        'invoice_form': invoice_form,
        'customers': customers
    }

    template = 'invoices/create_invoice.html'

    return render(request, template, context)


@login_required
def invoices(request):
    # View users bills
    invoices = Invoice.objects.filter(user=request.user)
    template = 'invoices/invoices.html'
    context = {
        'invoices': invoices
    }
    return render(request, template, context)


@login_required
def edit_invoice(request, invoice_number):
    # Edit Invoice
    invoice = Invoice.objects.get(invoice_number=invoice_number)
    invoiceLines = InvoiceLineItem.objects.filter(invoice=invoice)

    if request.method == "POST":
        form_data = {
            'user': request.user,
            'customer_account': request.POST['customer_account'],
            'invoice_date': request.POST['invoice_date'],
            'due_date': request.POST['due_date'],
            'reference_number': request.POST['reference_number'],
            'invoice_paid': request.POST.get('invoice_paid', False)
        }
        invoice_form = InvoiceForm(form_data, instance=invoice)
        if invoice_form.is_valid():
            invoice_form.save()
            messages.success(request, ("Invoice Successfully Updated!"))
            return redirect(reverse('profile'))

    customers = Customer.objects.filter(user=request.user)
    form = InvoiceForm(instance=invoice)

    template = 'invoices/edit_invoice.html'
    context = {
        'invoice': invoice,
        'invoiceLines': invoiceLines,
        'customers': customers,
        'form': form
    }

    return render(request, template, context)


@login_required
def delete_invoice(request, invoice_number):
    # Delete Invoice
    invoice = get_object_or_404(Invoice, invoice_number=invoice_number)
    invoice.delete()
    messages.success(request, ("Invoice Successfully Deleted!"))

    return redirect(reverse('profile'))
