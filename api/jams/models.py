from django.db import models

# Create your models here.

class Song(models.Model):
    name = models.CharField(default = 'Untitled', max_length=255)
    duration = models.FloatField(null = False)
    number_of_plays = models.IntegerField(default = 0, null = True)
    artist = models.ManyToManyField('Artist', blank = True, null = True, related_name = 'artist')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, null = True, blank = True)


class Artist(models.Model):
    name = models.CharField(default = 'Untitled', max_length=255)
    about = models.CharField(default = 'Untitled', max_length=1000)
    genre = models.ForeignKey('Genre', on_delete = models.CASCADE, null = True, blank = True)

class Genre(models.Model):
    name = models.CharField(default = 'Untitled', max_length=255)
    
class Album(models.Model):
    name = models.CharField(default = 'Untitled', max_length=255)
    release = models.IntegerField(null = False, max_length=4)
    song_name = models.ManyToManyField('Song')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, null = True, blank = True)

class Playlist(models.Model):
    name = models.CharField(default = 'Untitled', max_length=255)
    song_name = song_name = models.ManyToManyField('Song')