from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import BankUser


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = BankUser
        fields = ['username', 'email', 'password1']
