from django.core.management.base import BaseCommand, CommandError
from artist.models import Artist
from ._crawl_artists import get_certain_artists


class Command(BaseCommand):

    help = 'Populate all the artists from Web Gallery of Art'

    def handle(self, *args, **options):
        artists = get_certain_artists()
        for a in artists:
            try:
                Artist(last_name=a.last_name, first_name=a.first_name, born=a.born, died=a.died,
                       period=a.period, profession=a.profession, nationality=a.nationality).save()
                print('{}'.format(a.last_name))
            except Exception as e:
                print(Artist(last_name=a.last_name).id)
                print(e)
