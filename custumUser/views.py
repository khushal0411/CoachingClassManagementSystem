from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from .forms import InputForm
from django.contrib import messages
from django.shortcuts import render, redirect
from custumUser.models import OrgData
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
        organization        = request.POST.get('org')
        print(username)
        print(password)
        print(organization)
        user = authenticate(request, username=username, password=password, organization=organization)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return render(request, 'base.html')
        else:
            messages.info(request, f'account done not exit plz sign in')
    data= OrgData.objects.all()
    form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form, 'title': 'log in','data':data})

