from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Client


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Client
        fields = ("email", "first_name", "last_name", "phone")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Client
        fields = ("email", "first_name", "last_name", "phone")
