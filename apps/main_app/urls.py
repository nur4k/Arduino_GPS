from rest_framework.routers import DefaultRouter

from apps.main_app.views import ItemView, DriverView


router = DefaultRouter()
router.register('item', ItemView)
router.register('driver', DriverView)

urlpatterns = []

urlpatterns += router.urls
