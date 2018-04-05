from __future__ import unicode_literals, absolute_import
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt


def health_check(request):
    return HttpResponse("OK", status=200)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})
