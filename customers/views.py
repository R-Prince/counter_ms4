from django.shortcuts import render, get_list_or_404
from .models import Customer


# View users customers
def customers(request):
    customers = get_list_or_404(Customer, user=request.user)
    template = 'customers/customers.html'
    context = {
        'customers': customers
    }
    return render(request, template, context)
