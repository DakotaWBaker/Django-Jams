from django.urls import path
from .views import *

urlpatterns = [
    path('song/', SongAPIView.as_view()),
    path('song/<str:pk>', SongAPIView.as_view())
]