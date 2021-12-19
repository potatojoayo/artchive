from user.models import User


class PossessionQuerySetMixin:

    def get_queryset(self):

        user = self.request.user

        if user.is_admin:
            return self.model.objects.all()

        if self.model == User:
            return self.model.objects.filter(id=user.id)

        return self.model.objects.filter(user=user.id)
