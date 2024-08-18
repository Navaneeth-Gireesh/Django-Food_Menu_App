from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2']
        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'username' : 'Username',
            'email': 'Email Address',
            'password1' : 'Password', 
            'password2': 'Confirm Password'
        }