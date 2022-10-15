
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser



class InputForm(forms.Form):
    username = forms.CharField(max_length=200)
    #email = forms.EmailField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = MyUser
        fields = ['username', 'password']
