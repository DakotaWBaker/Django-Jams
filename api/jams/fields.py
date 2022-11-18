from rest_framework import serializers
from .models import *
print(models)
class GenreField(serializers.RelatedField):
    def to_internal_value(self, data):
        obj, created = Genre.objects.get_or_create(**data)
        return obj

    def to_representation(self, value):
        return {
            "name": value.name
        }

class ArtistField(serializers.RelatedField):
    def to_internal_value(self, data):
        obj, created = Artist.objects.get_or_create(**data)
        return obj

    def to_representation(self, value):
        return {
            "name": value.name
        }

class SongField(serializers.RelatedField):
    def to_internal_value(self, data):
        obj, created = Song.objects.get_or_create(**data)
        return obj

    def to_representation(self, value):
        return {
            "name": value.name,
            "duration": value.duration
        }

