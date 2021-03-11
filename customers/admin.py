from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    fields = ('user', 'customer_name',
                'customer_email', 'customer_phone_number', 'company_name',
                'company_street_address1', 'company_street_address2',
                'company_city', 'company_county',
                'company_postcode')

    list_display = ('user', 'company_name', 'customer_email',
                    'customer_phone_number', 'company_city')


admin.site.register(Customer, CustomerAdmin)
