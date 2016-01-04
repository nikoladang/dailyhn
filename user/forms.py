from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django import forms
from django.contrib.auth.models import User

from .models import Profile

class UserCreationForm():
    def clean_username(self):
        username = self.cleaned_data['username']
        disallowed = ('activate','create','disable','login','logout','password','profile')

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
