from rest_framework.permissions import BasePermission
from django.contrib.auth.models import AnonymousUser
from .models import User


class IsSelf(BasePermission):

    def has_object_permission(self, request, view, obj):

        user = request.user

        if user.is_admin:
            return True

        if isinstance(obj, User):
            return user == obj

        return user == obj.user


class IsNotLoggedIn(BasePermission):

    def has_permission(self, request, view):

        return isinstance(request.user, AnonymousUser)
