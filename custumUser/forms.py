
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser
from organisationData.models import OrgData



class InputForm(forms.ModelForm):
    #username            = forms.CharField(max_length=200)
    email              = forms.EmailField(max_length=255)
    password            = forms.CharField(widget=forms.PasswordInput())
    organization        = forms.ModelMultipleChoiceField(queryset=OrgData.objects.all())

    class Meta:
        model = MyUser
        fields = ['email', 'password', 'organization']

