from rest_framework import routers
from .views import BlockViewSet, DataLakeBlockDetail
from django.urls import path

router = routers.DefaultRouter()
router.register(r'blocks', BlockViewSet)

urlpatterns = [
  path('dl-blocks/<int:pk>/', DataLakeBlockDetail.as_view())
]

urlpatterns += router.urls