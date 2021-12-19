from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from .models import Artist
from .serializers import ArtistSerializer
from .filters import ArtistFilter

# ReadOnlyModelViewSet:
# ModelViewSet과는 달리 'read-only' 액션만 가능


class ArtistViewSet(ReadOnlyModelViewSet):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [AllowAny]
    filterset_class = ArtistFilter
