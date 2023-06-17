from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Client

class RegisterForm(UserChangeForm):

    class Meta:
        model=Client
        fields = ['first_name', 'last_name', 'phone','email','password1','password2']

    email = forms.CharField(min_length=6, max_length=65, required=True, widget=forms.TextInput(
                            attrs={'placeholder': 'Your Email',
                                    'type': 'email'}))
    first_name = forms.CharField(min_length=1, max_length=50, required=True, widget=forms.TextInput(
                            attrs={'placeholder': 'Your First Name'}))
    last_name = forms.CharField(min_length=1,max_length=50, required=True, widget=forms.TextInput(
                            attrs={'placeholder': 'Your Last Name'}))
    phone = forms.CharField(min_length=9, max_length=9, required=False, widget=forms.TextInput(
                            attrs={'placeholder': 'Your Phone'}))
    password1 = forms.CharField(min_length=8, max_length=65, required=True, widget=forms.PasswordInput(
                            attrs={'placeholder': 'Your Password'}))
    password2 = forms.CharField(min_length=8, max_length=65, required=True, widget=forms.PasswordInput(
                            attrs={'placeholder': 'Repeat Password'}))

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Client
        fields = ("email", "first_name", "last_name", "phone")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Client
        fields = ("email", "first_name", "last_name", "phone")
        
class LoginForm(forms.Form):
    email = forms.CharField(min_length=6, max_length=65, required=True, widget=forms.TextInput(
                            attrs={'class': "form-control"}))
    password = forms.CharField(min_length=6, max_length=65, widget=forms.PasswordInput(
                            attrs={'class':   "form-control"}))
