from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomerCreationForm, LoginForm, CustomerUpdateForm


def register(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomerCreationForm()
    return render(request, 'customer/register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Bem vindo, {user.username}!')

                next_page = request.GET.get('next', 'index')
                return redirect(next_page)
    else:
        form = LoginForm()
    return render(request, 'customer/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, 'Você saiu do sistema.')
    return redirect('index')

@login_required(login_url='customer/register/')
def profile_view(request):
    return render(request, 'customer/profile_view.html')

@login_required(login_url='customer/register/')
def profile_edit(request):
    if request.method == 'POST':
        u_form = CustomerUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('profile_view')
    else:
        u_form = CustomerUpdateForm(instance=request.user)
    return render(request, 'customer/profile_edit.html', {'u_form': u_form })