from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django import forms
from django.contrib.auth.models import User

from .models import Profile

# class UserCreationForm():
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         disallowed = ('activate','create','disable','login','logout','password','profile')
#
# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
#
# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('date_of_birth', 'photo')
#
#
#
#
# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

#http://localhost:8000/accounts/signup/
class SignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phone', 'age')

    def signup(self, request, user):
        user.username = "xxzxzxz"
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.age = self.cleaned_data['age']
        user.save()

        profile = Profile()
        profile.user = user
        profile.phone = self.cleaned_data['phone']
        profile.age = self.cleaned_data['age']
        profile.save()