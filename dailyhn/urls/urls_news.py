from django.conf.urls import url

urlpatterns = [
    url(r'^$',
        'dailyhn.views.views_news.newsapi_home',
        name="newsapi_home"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        'dailyhn.views.views_news.newsapi_home_adate',
        name="newsapi_home_adate"),
]