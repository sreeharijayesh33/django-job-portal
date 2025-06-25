from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, RoleEnum

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Full Name', 'class': 'form-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email', 'class': 'form-control'
    }))
    phone_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={
        'placeholder': 'Phone Number', 'class': 'form-control'
    }))
    role = forms.ChoiceField(choices=RoleEnum.choices(), widget=forms.Select(attrs={
        'class': 'form-select'
    }))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone_number', 'role', 'password1', 'password2']
