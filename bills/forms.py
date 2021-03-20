from django import forms
from .models import Bill, BillLineItem


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = (
            'customer_account', 'bill_date', 'due_date',
            'reference_number', 'bill_paid',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'customer_account': 'Customer Account',
            'bill_date': 'Bill Date',
            'due_date': 'Due Date',
            'reference_number': 'Reference Number',
            'bill_paid': 'Bill Paid?',
        }

        self.fields['customer_account'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'bill-form'
            self.fields[field].label = False


class BillLineForm(forms.ModelForm):
    class Meta:
        model = BillLineItem
        fields = ('description', 'quantity', 'price', 'item_tax',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
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
            self.fields[field].widget.attrs['class'] = 'bill-line-form'
            self.fields[field].label = False
