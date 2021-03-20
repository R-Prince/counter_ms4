from django.contrib import admin
from .models import Bill, BillLineItem


# Bill line item Admin
class BillLineItemAdminInline(admin.TabularInline):
    model = BillLineItem
    readonly_fields = ('item_total',)


# Bill Admin
class BillAdmin(admin.ModelAdmin):
    inlines = (BillLineItemAdminInline,)

    readonly_fields = ('bill_number', 'bill_total',)

    fields = ('user', 'bill_number', 'customer_account', 'bill_date',
              'due_date', 'reference_number', 'bill_paid',
              'bill_total',)

    ordering = ('-bill_date',)


admin.site.register(Bill, BillAdmin)
