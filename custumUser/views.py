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
        username            = request.POST.get('email')
        password            = request.POST['password']
        organization        = request.POST.get('org')
        user = authenticate(request, email=username, password=password, organization=organization)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            org= OrgData.objects.filter(OrgName=organization)
            return render(request, 'base.html',{'username':username,'organization':organization,'org':org})
        else:
            messages.info(request, f'account done not exit plz sign in')
    data= OrgData.objects.all()
    #form = AuthenticationForm()
    return render(request, 'signin.html', { 'title': 'log in','data':data})


def home(request):

    return render(request, 'home.html')

