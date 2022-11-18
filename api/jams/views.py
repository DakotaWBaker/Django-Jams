from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response

# Create your views here.


class SongViewSet(ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class SongArtistViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_queryset(self):
        if self.request.artist.name:
            queryset = Song.objects.filter(artist=self.request.artist.name)
            return queryset.order_by('artist')
        else:
            return queryset
   
    # def get_queryset(self):
    #     artist_name = self.request.query_params.get('name')
    #     return Song.objects.filter(artist__name = name)
       
