from rest_framework import routers
from django.urls import path, include
from .viewsets import WorkViewSet

router = routers.DefaultRouter()
router.register('work', WorkViewSet, basename='work')

urlpatterns = [path('', include(router.urls))]
