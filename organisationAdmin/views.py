from django.shortcuts import render


# Create your views here.

def dashboard(request):

    return render(request, 'dashboard.html')

def registerStuTea(request):

    return render(request, 'registerStuTea.html')