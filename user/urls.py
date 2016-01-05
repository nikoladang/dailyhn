from django.conf.urls import url

urlpatterns = [
    url(r'^loginz/$',
        'django.contrib.auth.views.login',
        name='login'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout'),
    url(r'^logout-then-login/$',
        'django.contrib.auth.views.logout_then_login',
        name='logout_then_login')
]