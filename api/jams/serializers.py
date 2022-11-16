from rest_framework import serializers
from .models import *
from pprint import pprint as p




class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name",)

class ArtistSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    class Meta:
        model = Artist
        fields = ('name', 'about', 'genre')

    def create(self, validated_data):
       genre = validated_data.pop('genre')
       genre_instance = Genre.objects.get(name = genre['name'])
       artist = Artist.objects.create(**validated_data, genre = genre_instance)
       return artist

class SongSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    class Meta:
        model = Song
        fields = ('name', 'duration', 'number_of_plays', 'genre')
