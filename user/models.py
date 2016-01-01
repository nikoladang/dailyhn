from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractUser, AbstractBaseUser
)
# Create your models here.
# genders = ["Male", "Female", "Other"]

genders = (
    (1, "Female"),
    (2, "Male"),
    (3, "Other"),
)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']


# class CustomUser(AbstractUser):
#     age = models.PositiveIntegerField(null=True, blank=True)
#     gender = models.CharField(choices=genders,
#                               default="Female",
#                               max_length=20, blank=True)
#     REQUIRED_FIELDS = ['email']
#     pass