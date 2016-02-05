"""dailyhn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic.simple import direct_to_template
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from dailyhn.api.viewsets_entry import EntryViewSet
from dailyhn.api.viewsets_user import UserViewSet
# from dailyhn import api


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entry', EntryViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'dailyhn.views.entry_views.newsapi_home', name="newsapi_home"),
    url(r'^auth/', include('authtools.urls')),
    url(r'^accounts/', include('allauth.urls')),
    # url(r'^accounts/profile/', 'dailyhn.views.get_profile', name="user_profile"),
    url(r'^profile/$', 'dailyhn.views.entry_views.profile_view', name="user_profile"),
    url(r'^user/', include('user.urls')),
    url(r'^news/', include('dailyhn.urls.entry_urls')),
    url(r'^bookmark/', include('dailyhn.urls.bookmark_urls')),

    # api
    url(r'^api/', include('dailyhn.apiv1')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)