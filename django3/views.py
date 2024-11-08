# views.py
from django.shortcuts import render, redirect
from .models import Customer
from .forms import SubscribeForm
from django.contrib import messages

def subscribe_view(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            Customer.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            )
            messages.success(request, 'You have successfully subscribed!')
            return redirect('subscribe')
        else:
            messages.error(request, 'Failed to subscribe. Please check the form and try again.')
    else:
        form = SubscribeForm()

    return render(request, 'subscribe.html', {'form': form})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

