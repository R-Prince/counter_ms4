from django.contrib import admin
from .models import Invoice, InvoiceItem, InvoiceStatus


class InvoiceItemAdmin(admin.TabularInline):
    model = InvoiceItem
    readonly_fields = ('item_total',)


class InvoiceStatusAdmin(admin.TabularInline):
    model = InvoiceStatus
    readonly_fields = ('paid',)


class InvoiceAdmin(admin.ModelAdmin):
    inlines = (InvoiceItemAdmin, InvoiceStatusAdmin,)
    readonly_fields = (
        'invoice_total',
    )

    fields = (
        'user', 'date_created', 'due_date', 'invoice_number',
        'customer_account', 'invoice_total')

    list_display = (
        'user', 'date_created', 'due_date',
        'invoice_number', 'invoice_total')


admin.site.register(Invoice, InvoiceAdmin)
