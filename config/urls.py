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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'news.views.newsapi_home', name="newsapi_home"),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/', 'news.views.get_profile', name="user_profile"),
    url(r'^news/$', 'news.views.newsapi_home', name="newsapi_home"),
    url(r'^news/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'news.views.newsapi_home_adate', name="newsapi_home_adate"),
    url(r'^user/', include('user.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)