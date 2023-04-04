from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

# Views


def home(request):
    return render(request, "account/home.html", {})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            firstname= form.cleaned_data.get('firstname')
            lastname= form.cleaned_data.get('lastname')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(firstname=firstname, lastname=lastname, username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})
