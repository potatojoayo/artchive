from django.core.management.base import BaseCommand
from django.db.models import Count
from work.models import Work
from artist.models import Artist
from ._crawl_works import get_works
# import requests
# import boto3


# s3 = boto3.resource('s3')
# bucket = s3.Bucket('artchivepotatojoayo')


class Command(BaseCommand):

    help = 'Populate works by lastname of an artist from Web Gallery of Art'

    def add_arguments(self, parser):
        parser.add_argument('last_name', type=str,
                            help='The last name of an artist you want to add')
        parser.add_argument('first_name', type=str,
                            help='The first name of an artist you want to add')
        parser.add_argument('keyword', type=str,
                            help='The keyword of an artist you want to add')

    def handle(self, *args, **options):
        last_name = options['last_name']
        first_name = options['first_name']
        keyword = options['keyword']
        a = Artist.objects.filter(
            last_name__icontains=last_name, first_name__icontains=first_name)[0]
        works = get_works(keyword)
        for w in works:
            try:
                # r = requests.get(w.image, stream=True)
                # bucket.upload_fileobj(
                #    r.raw, (w.name+'_'+a.last_name).replace(' ', '_')+'.jpg')
                Work(artist=a, name=w.name, start_year=w.start_year, finish_year=w.finish_year,
                     info=w.info, location=w.location, image=w.image).save()
            except Exception as e:
                print(e)

            print(w.name + ' is inserted / artist id = ' + str(a.id))
