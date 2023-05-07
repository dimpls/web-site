from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'phone_number',)
        widgets = {
            'email': forms.TextInput(attrs={'type': 'email'})
        }


