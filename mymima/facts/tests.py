from django.test import TestCase
from . import models
import datetime

from django.test import TestCase
from django.utils import timezone


# Create your tests here
class ArtistModelTests(TestCase):
    def test_data_saved(self):
        q = models.Artist(artist_first_name='Dodo', artist_last_name='Tasa')
        q.save()
        data = models.Artist.objects.all()
        self.assertIs(len(data) != 0, True)

    def test_relationships_artist_song(self):
        q = models.Artist(artist_first_name='Dodo', artist_last_name='Tasa')
        q.save()
        s = models.Song.objects.create(artist=q, song_name='Maaliot')
        self.assertIs(s.artist.artist_first_name, 'Dodo')
