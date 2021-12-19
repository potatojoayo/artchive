from rest_framework import routers
from django.urls import path, include
from .viewsets import LikeViewSet

router = routers.DefaultRouter()
router.register('like', LikeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
