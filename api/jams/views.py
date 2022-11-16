from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
# Create your views here.

class SongAPIView(APIView):
    #Read ops
    def get_object(self, pk):
        try: 
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = SongSerializer(data)
        else:
            data = Song.objects.all()           #Can use order by or filter here
            serializer = SongSerializer(data, many=True)

        return Response(serializer.data)

    #Create ops
    def post(self, request, format=None):
        print('You sent a post request')
        data = request.data
        serializer = SongSerializer(data=data)

        #Check if data is valid
        serializer.is_valid(raise_exception=True)

        #Save songs sent over
        serializer.save()

        #Inform front-end of result
        response = Response()

        response.data = {
            'message': "Song created",
            'data': serializer.data
        }

        return response

        #def put
        #def delete
class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ['get', 'post']

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    http_method_names = ['get', 'post']


