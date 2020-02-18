import datetime

from django.db import models
from django.utils import timezone


class Artist(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'

class Facts(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    fact = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.fact}'