from django.contrib.auth.models import User
from django import forms
from .models import Perfil

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["telefono", "foto"]

