from django import forms
from .models import Invoice, InvoiceItem, InvoiceStatus


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = (
            'date_created', 'due_date',
            'invoice_number',
            'customer_account', 'invoice_total')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'date_created': 'Invoice Date',
            'due_date': 'Due Date',
            'invoice_number': 'Invoice Number',
            'customer_account': 'Customer Account',
        }

        self.fields['customer_account'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-input'
            self.fields[field].label = False


class InvoiceLineForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = (
            'description', 'quantity',
            'price',
            'item_tax', 'item_total')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'description': 'Item Description',
            'quantity': 'Qty',
            'price': 'Price',
            'item_tax': 'Item Tax',
            'item_total': 'Item Total',
        }

        self.fields['description'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-input'
            self.fields[field].label = False


class InvoiceStatusForm(forms.ModelForm):
    class Meta:
        model = InvoiceStatus
        fields = (
            'paid', 'date_paid'
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'date_paid': 'Date Paid',
        }

        self.fields['date_paid'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-input'
            self.fields[field].label = False
