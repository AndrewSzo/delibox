from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required()
def customer_page(request):
    return render(request, 'customer/customer_base.html')


