from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=250)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1']
        labels = {
            'first_name': 'First name:',
            'last_name': 'Last name:',
            'username': 'Username:',
            'email': 'E-mail address:',
            'password1': 'Password1:'
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'description']
