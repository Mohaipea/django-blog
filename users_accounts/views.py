from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.shortcuts import render, redirect


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
    pass


def logoutPage(request):
    logout(request)
    return redirect('home')