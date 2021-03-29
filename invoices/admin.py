from django.contrib import admin
from .models import Invoice, InvoiceLineItem


# Invoice line item Admin
class InvoiceLineItemAdminInline(admin.TabularInline):
    model = InvoiceLineItem
    readonly_fields = ('item_total',)


# Invoice Admin
class InvoiceAdmin(admin.ModelAdmin):
    inlines = (InvoiceLineItemAdminInline,)

    readonly_fields = ('invoice_number', 'invoice_total',)

    fields = ('user', 'invoice_number', 'customer_account', 'inv_date',
              'due_date', 'reference_number', 'invoice_paid',
              'invoice_total',)

    ordering = ('-invoice_date',)


admin.site.register(Invoice, InvoiceAdmin)
