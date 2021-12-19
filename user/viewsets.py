from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from .serializers import UserSerializer, RegisterSerializer
from .models import User
from .permissions import IsSelf, IsNotLoggedIn
from .mixins import PossessionQuerySetMixin


class UserViewSet(PossessionQuerySetMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin,  UpdateModelMixin, DestroyModelMixin):

    model = User

    def get_serializer_class(self):

        if self.action == 'create':
            return RegisterSerializer
        return UserSerializer

    def get_permissions(self):

        if self.action == 'create':
            permission_classes = [IsNotLoggedIn]
        else:
            permission_classes = [IsAuthenticated,  IsSelf]
        return [permission() for permission in permission_classes]
