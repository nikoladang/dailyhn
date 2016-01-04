
from django.shortcuts import render
from django.http import HttpResponse
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from .models import Profile
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.
@receiver(user_signed_up)
def set_gender(sender, **kwargs):
    user = kwargs.pop("user")
    extra_data = user.socialaccount_set.filter(provider="facebook")[0].extra_data
    gender = extra_data['gender']

    if gender == "Male":
        user.gender = "Male"
    print("Inside set_gender")
    user.save()

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated ' \
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

