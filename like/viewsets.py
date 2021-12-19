from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeViewSet(ModelViewSet):

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ('user_id', 'artist_id', 'work_id', 'comment_id')
