from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, AbstractUser
)
from django_countries.fields import CountryField
from sorl.thumbnail import ImageField
# # Create your models here.
# # genders = ["Male", "Female", "Other"]
#
# genders = (
#     (1, "Female"),
#     (2, "Male"),
#     (3, "Other"),
# )
#
# class MyUserManager(BaseUserManager):
#     def create_user(self, email, date_of_birth, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(
#             email=self.normalize_email(email),
#             date_of_birth=date_of_birth
#         )
#         user.set_password=password
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, date_of_birth, password):
#         user = self.create_user(
#             email,
#             password=password,
#             date_of_birth=date_of_birth
#         )
#         user.is_admin=True
#         user.save(using=self._db)
#         return user
#
# class MyUser(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True
#     )
#     date_of_birth = models.DateField()
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#
#     objects = MyUserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['date_of_birth']
#
#     def get_full_name(self):
#         return self.email
#
#     def get_short_name(self):
#         return self.email
#
#     def __str__(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         return True
#
#     def has_module_perms(self, app_label):
#         return True
#
#     @property
#     def is_staff(self):
#         return self.is_admin
#
#     # USERNAME_FIELD = 'email'
#     # REQUIRED_FIELDS = ['email']
#
#
# # class CustomUser(AbstractUser):
# #     age = models.PositiveIntegerField(null=True, blank=True)
# #     gender = models.CharField(choices=genders,
# #                               default="Female",
# #                               max_length=20, blank=True)
# #     REQUIRED_FIELDS = ['email']
# #     pass
#
# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL)
#     date_of_birth = models.DateField(blank=True, null=True)
#     photo = models.ImageField(upload_to='user/%Y/%m/%d')
#
#     def __str__(self):
#         return ""

# # http://www.rawrers.org/?p=867
# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)
#     age = models.CharField(max_length=100)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    country = CountryField()
    entries_per_day = models.IntegerField(default=10)
    days_at_homepage = models.IntegerField(default=3)
    icon_symbol = models.ImageField(upload_to='icon_symbol/%Y/%m/%d', blank=True, null=True)
    # icon_symbol = ImageField(upload_to='icon_symbol/%Y/%m/%d', blank=True, null=True)
    # icon_bookmark = models.ImageField(upload_to='icon_bookmark/%Y/%m/%d', width_field='32', height_field='32' ,blank=True, null=True)
    icon_bookmark = models.ImageField(upload_to='icon_bookmark/%Y/%m/%d', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.user)