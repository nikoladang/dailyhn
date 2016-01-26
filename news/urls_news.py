from django.conf.urls import url

urlpatterns = [
    url(r'^$',
        'news.views.newsapi_home',
        name="newsapi_home"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        'news.views.newsapi_home_adate',
        name="newsapi_home_adate"),
]