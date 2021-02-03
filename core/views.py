from django.contrib.auth import login
from django.shortcuts import render, redirect
from . import forms


def home(request):
    return render(request, 'home.html')


def register_page(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email').lower()
            user = form.save(commit=False)
            user.username = email
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
    return render(request, 'register.html', { 'form':form })

