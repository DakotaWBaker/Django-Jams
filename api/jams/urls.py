from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('artist', ArtistViewSet)
router.register('album', AlbumViewSet)
router.register('song', SongViewSet)
router.register('playlist', PlaylistViewSet)
artist_filter =  SongArtistViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('song/<artist>/', artist_filter),
    path('', include(router.urls))
]