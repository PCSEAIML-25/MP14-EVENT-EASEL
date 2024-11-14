from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Enter username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Enter password"
            }
        )
    )

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Enter username"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Enter Password"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Confirm Password"
            }
        )
    )
    
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Enter email"
            }
        )
    )

    branch = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Enter Branch"
            }
        )
    )

    library_ID = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Enter Library ID"
            }
        )
    )

    github = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Enter Github Profile"
            }
        )
    )


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'branch', 'library_ID', 'github', 'is_coordinator')
    
