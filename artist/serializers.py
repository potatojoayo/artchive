from rest_framework import serializers
from .models import Artist
from work.serializers import WorkSerializer


class ArtistSerializer(serializers.ModelSerializer):

    works = WorkSerializer(many=True, read_only=True)

    class Meta:

        model = Artist
        fields = '__all__'
