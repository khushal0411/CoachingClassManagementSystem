from django.urls import path

import organisationAdmin.views
from . import views
from organisationAdmin.views import dashboard

urlpatterns = [
    path('',views.home_view, name="signin"),
    #path('signin/', views.home_view, name="signin"),
    path('base/', views.home_view, name="base"),
    path('dashboard/', organisationAdmin.views.dashboard, name="dashboard")
]
