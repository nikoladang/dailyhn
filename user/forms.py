from django.core.exceptions import ValidationError
from django.utils.text import slugify

from .models import Profile

class UserCreationForm():
    def clean_username(self):
        username = self.cleaned_data['username']
        disallowed = ('activate','create','disable','login','logout','password','profile')