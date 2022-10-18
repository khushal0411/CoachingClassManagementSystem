from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from .forms import InputForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


# Create your views here.
"""def home_view(request):
    context = {'form': InputForm()}
    return render(request, "authentication/signin.html", context)"""



def home_view(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username            = request.POST['username']
        password            = request.POST['password']
        organization        = request.POST['organization']
        user = authenticate(request, username=username, password=password, organization=organization)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('/base/')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form, 'title': 'log in'})

