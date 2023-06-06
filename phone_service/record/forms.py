from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Client


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Client
        fields = ("email", "first_name", "last_name", "phone")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Client
        fields = ("email", "first_name", "last_name", "phone")
        
class LoginForm(forms.Form):
    email = forms.CharField(max_length=65, required=True, widget=forms.TextInput(
                            attrs={'class': "form-control"}))
    password = forms.CharField(max_length=65, widget=forms.PasswordInput(
                            attrs={'class':   "form-control"}))
