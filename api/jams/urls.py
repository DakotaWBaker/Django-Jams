from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('artist', ArtistViewSet)

urlpatterns = [
    path('song/', SongAPIView.as_view()),
    path('song/<str:pk>', SongAPIView.as_view()),
    path('', include(router.urls))
]