from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('signin/', views.home_view, name="signin"),
    path('base/', views.home_view, name="base")
]
