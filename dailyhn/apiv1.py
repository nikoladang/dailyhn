# from rest_framework import routers
#
# from .api.viewsets_entry import EntryViewSet
#
# router = routers.DefaultRouter()
# # router.register(r'users', UserViewSet)
# router.register(r'^entry', EntryViewSet, base_name='entry')

from django.conf.urls import url, include
from rest_framework import routers
from .api.viewsets_entry import EntryViewSet

router = routers.DefaultRouter()
# router.register()
router.register(r'entry', EntryViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]