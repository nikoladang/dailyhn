from django.contrib import admin
# from .models import Profile
from .models import UserProfile

# # Register your models here.
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['user', 'date_of_birth', 'photo']

class ProfileAdmin(admin.ModelAdmin):
    # list_display = ['user', 'phone']
    list_display = ['user', 'country']

admin.site.register(UserProfile, ProfileAdmin)

