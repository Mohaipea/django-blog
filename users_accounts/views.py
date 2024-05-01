from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect

from users_accounts.forms import RegistrationForm


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        raise Http404('کاربر مورد نظر یافت نشد')

    context = {'page': 'login'}
    return render(request, 'users_accounts/login_register.html', context)


def registerPage(request):
    regisetr_form = RegistrationForm(request.POST or None)
    if regisetr_form.is_valid():
        username = regisetr_form.cleaned_data.get('username')
        email = regisetr_form.cleaned_data.get('email')
        password = regisetr_form.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return redirect('home')

    context = {'page': 'register', 'form': regisetr_form}
    return render(request, 'users_accounts/login_register.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')