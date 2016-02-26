from django.conf.urls import url
from ..views.entry_views import EntryListView

urlpatterns = [
    url(r'^$',
        'dailyhn.views.entry_views.newsapi_home',
        name="newsapi_home"),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        'dailyhn.views.entry_views.newsapi_home_adate',
        name="newsapi_home_adate"),
    url(r'^list/$',
        EntryListView.as_view(),
        name='entry-list')
]