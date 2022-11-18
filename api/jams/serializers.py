from rest_framework import serializers, filters
from .models import *
from .fields import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name",)


class ArtistSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = Artist
        fields = ("name", "about", "genre")

    def create(self, validated_data):
        genre = validated_data.pop("genre")
        genre_instance = Genre.objects.get(name=genre["name"])
        artist = Artist.objects.create(**validated_data, genre=genre_instance)
        return artist


class SongSerializer(serializers.ModelSerializer):
    genre = GenreField(queryset=Genre.objects.all())
    artist = ArtistField(many=True, queryset=Artist.objects.all())
    album_name = Song.album_name
    print(album_name)
    

    class Meta:
        model = Song
        fields = ("id", "name", "duration", "number_of_plays", "genre", "artist", 'album_name')


class AlbumSerializer(serializers.ModelSerializer):
    song_name = SongField(many=True, queryset=Song.objects.all())
    class Meta:
        model = Album
        fields = ("name", "release", "song_name")
   
class PlaylistSerializer(serializers.ModelSerializer):
    song_name = SongField(many=True, queryset=Song.objects.all())
    class Meta:
        model = Playlist
        fields = ("name", "song_name")

class ArtistFilter(serializers.ModelSerializer):
    
    class Meta:
        model = Song
        fields = "__all__"
