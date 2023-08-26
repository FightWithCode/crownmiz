from rest_framework import serializers
from core.models import Song, Movie


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
