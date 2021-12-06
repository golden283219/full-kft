from rest_framework.routers import SimpleRouter

from notifications.views import NotificationViewSet

router = SimpleRouter()
router.register("", NotificationViewSet, basename="notification")

urlpatterns = router.urls
