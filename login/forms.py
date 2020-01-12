from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserAccount, ch_type

# Authentication Forms
class SigninForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(min_length=8, max_length=150, widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    account_type = forms.CharField(max_length=64, required=True, widget=forms.Select(choices=ch_type))
    email = forms.CharField(max_length=200, required=True, help_text="This email will be used for contact info.")

    class Meta:
        model = User
        fields = ('username', 'account_type', 'email', 'password1', 'password2',)