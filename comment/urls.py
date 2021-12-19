from rest_framework import routers
from django.urls import path, include
from .viewsets import CommentViewSet

router = routers.DefaultRouter()
router.register('comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
