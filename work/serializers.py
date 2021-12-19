from rest_framework import serializers
from .models import Work
from comment.serializers import CommentSerializer
from like.serializers import LikeSerializer


class WorkSerializer(serializers.ModelSerializer):

    artist = serializers.SerializerMethodField()

    class Meta:

        model = Work
        fields = '__all__'

    def get_artist(self, instance):
        from artist.serializers import ArtistSerializer
        return ArtistSerializer(instance.artist).data
