from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from accounts.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    buissness_name = forms.CharField(max_length=100)
    buissness_logo = forms.ImageField(upload_to='logo')
    address_line1 = forms.CharField(max_length=50)
    city = forms.CharField(max_length=20)
    state = forms.CharField(max_length=20)
    pincode = forms.IntegerField(null=True)

    class Meta:
        model = User
        fields = ('email', 'buissness_name', 'buissness_logo', 'address_line1',
                  'city', 'state', 'pincode', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            user = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} already in use.')

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f'Username {username} already in use.')
