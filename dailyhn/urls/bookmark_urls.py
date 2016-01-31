from django.conf.urls import url
from dailyhn.views.bookmark_views import BookmarkListView


urlpatterns = [
    url(r'^list/$', BookmarkListView.as_view(), name="bookmark_list_view")
]
