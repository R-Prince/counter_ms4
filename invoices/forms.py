from django import forms
from .models import Invoice, InvoiceLineItem


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = (
            'user',
            'customer_account', 'invoice_date', 'due_date',
            'reference_number', 'invoice_paid',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user': 'Username',
            'customer_account': 'Customer Account',
            'invoice_date': 'Date (YYYY-MM-DD)',
            'due_date': 'Due (YYYY-MM-DD)',
            'reference_number': 'Reference Number',
            'invoice_paid': 'Invoice Paid?',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'invoice-form'
            self.fields[field].label = False


class InvoiceLineForm(forms.ModelForm):
    class Meta:
        model = InvoiceLineItem
        fields = ('invoice', 'description', 'quantity', 'price', 'item_tax',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'invoice': 'Invoice',
            'description': 'Item Description',
            'quantity': 'Qty',
            'price': 'Item Price',
            'item_tax': 'Item Tax',
        }

        self.fields['description'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'invoice-line-form'
            self.fields[field].label = False
