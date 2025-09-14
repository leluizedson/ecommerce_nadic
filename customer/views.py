from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'customer/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'customer/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required(login_url='customer/register/')
def profile_view(request):
    return render(request, 'customer/profile_view.html')

@login_required(login_url='customer/register/')
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('profile_view')
    else:
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'customer/profile_edit.html', {'u_form': u_form })