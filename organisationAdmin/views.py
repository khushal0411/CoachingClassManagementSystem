from django.shortcuts import render


# Create your views here.
from organisationData.models import OrgData


def dashboard(request):
    if request.user is not None:
        org = OrgData.objects.filter(OrgName=request.user.organization)
        return render(request, 'dashboard.html',{'username':request.user.username,'organization':request.user.organization,'org':org})


def registerStuTea(request):
    if request.user is not None:
        org = OrgData.objects.filter(OrgName=request.user.organization)
        return render(request, 'registerStuTea.html',{'username':request.user.username,'organization':request.user.organization,'org':org})
