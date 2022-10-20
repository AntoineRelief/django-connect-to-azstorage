from rest_framework import routers
from .views import BlockViewSet

router = routers.DefaultRouter()
router.register(r'blocks', BlockViewSet)

urlpatterns = router.urls