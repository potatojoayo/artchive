from rest_framework import routers
from django.urls import path, include
from .viewsets import UserViewSet
from .views import LoginView

router = routers.DefaultRouter()
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view())
]
