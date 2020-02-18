from facts.models import Artist, Song, Facts
import requests
from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup


class Command(BaseCommand):
    help = "Take all data needed from mima"

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, n, *args, **options):
        Facts.objects.all().delete()
        Song.objects.all().delete()
        Artist.objects.all().delete()
        for i in range(1, n):
            # print(i,'befor')
            r = requests.get(f"https://www.mima.co.il/fact_page.php?song_id={i}").text
            # print(i,'after')
            soup = BeautifulSoup(r, "html.parser")
            for ti in soup.find_all("title"):
                all_data = ti.text.split(' - ')
                artist = all_data[1]
                song = all_data[2][:-1]
                facts = []
                for fa in soup.find_all('tr'):
                    if fa.get('bgcolor'):
                        facts.append(fa.text)
                o,b = Artist.objects.get_or_create(name=artist)
                o.save()
                # print((Artist.objects.all()[0]))
                o1 = Song(name=song, artist=o)
                o1.save()
                if facts:
                    for fact in facts:
                        o2,b = Facts.objects.get_or_create(song=o1, fact=fact)
                        o2.save()




