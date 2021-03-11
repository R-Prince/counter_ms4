from django.shortcuts import render


# View users customers
def customers(request):
    template = 'customers/customers.html'
    context = {
    }
    return render(request, template, context)
