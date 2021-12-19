from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import WorkSerializer
from .models import Work
from .filters import WorkFilter


class WorkViewSet(ReadOnlyModelViewSet):

    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filterset_class = WorkFilter
