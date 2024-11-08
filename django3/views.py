# views.py
from django.shortcuts import render, redirect
# from .forms import SubscribeForm
from .models import Customer
from .forms import SubscribeForm
from django.contrib import messages

def subscribe_view(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            # Simpan data ke database
            Customer.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            )
            messages.success(request, 'You have successfully subscribed!')
            return redirect('subscribe')  # Redirect kembali ke halaman subscribe
        else:
            messages.error(request, 'Failed to subscribe. Please check the form and try again.')
    else:
        form = SubscribeForm()

    return render(request, 'subscribe.html', {'form': form})
