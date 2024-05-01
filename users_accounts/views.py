from django.shortcuts import render


def loginPage(request):
    context = {}
    return render(request, '', context)
