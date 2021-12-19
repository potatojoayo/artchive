from django.core.management.base import BaseCommand, CommandError
from artist.models import Artist
from ._crawl_artists import get_all_artists


class Command(BaseCommand):

    help = 'Populate all the artists from Web Gallery of Art'

    def handle(self, *args, **options):
        artists = get_all_artists()
        for index, a in enumerate(artists):
            try:
                Artist(last_name=a.last_name, first_name=a.first_name, born=a.born, died=a.died,
                       period=a.period, profession=a.profession, nationality=a.nationality).save()
                print('{} {} was succesfully inserted. {}/{}'.format(a.first_name,
                      a.last_name, index, len(artists)))
            except Exception as e:
                print(e)
