from rest_framework import routers
from django.urls import path, include
from .viewsets import ArtistViewSet

router = routers.DefaultRouter()
router.register('artist', ArtistViewSet, basename='artist')

urlpatterns = [
    path('', include(router.urls))
]
