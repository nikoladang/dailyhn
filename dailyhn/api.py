from rest_framework import routers

from .api.viewsets_entry import EntryViewSet

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'^entry', EntryViewSet, base_name='entry')
urlpatterns = router.urls