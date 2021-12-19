from django.core.management.base import BaseCommand
from work.models import Work
from artist.models import Artist
from ._crawl_works import get_works
#import requests
#import boto3
from work.models import Work


#s3 = boto3.resource('s3')
#bucket = s3.Bucket('artchivepotatojoayo')


class Command(BaseCommand):

    help = 'Populate works by lastname of an artist from Web Gallery of Art'

    def handle(self, *args, **options):
        artists = Artist.objects.filter(id__gte=0)
        for index, a in enumerate(artists):
            works = get_works(a.last_name)
            for w in works:
                try:
                    #r = requests.get(w.image, stream=True)
                    # bucket.upload_fileobj(
                    #    r.raw, (w.name+'_'+a.last_name).replace(' ', '_')+'.jpg')
                    Work(artist=a, name=w.name, start_year=w.start_year, finish_year=w.finish_year,
                         info=w.info, location=w.location, image=w.image).save()
                    print('{} [{}] was successfuly inserted. {}/{}'.format(w.name,
                          a.last_name, index, len(artists)))
                except Exception as e:
                    print(e)
