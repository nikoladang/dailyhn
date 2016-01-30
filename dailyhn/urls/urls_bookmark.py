from django.conf.urls import url
from dailyhn.views.views_bookmark import BookmarkListView


urlpatterns = [
    url(r'^list/$', BookmarkListView.as_view(), name="bookmark_list_view")
]
