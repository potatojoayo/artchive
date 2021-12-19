from django.core.management.base import BaseCommand
from django.db.models import Count
from work.models import Work
from artist.models import Artist
from ._crawl_works import get_works
import requests
import boto3


def url(lastname):
    return 'https://www.wga.hu/cgi-bin/search.cgi?author={}&time=any&school=any&form=any&type=any&title=&comment=&location=&from=0&max=1000&format=5'.format(lastname)


s3 = boto3.resource('s3')
bucket = s3.Bucket('artchivepotatojoayo')


class Command(BaseCommand):

    help = 'Populate works by lastname of an artist from Web Gallery of Art'

    def handle(self, *args, **options):
        artists = Artist.objects.annotate(count=Count('works')).filter(count=0)
        for a in artists:
            works = get_works(a.last_name)
            for w in works:
                try:
                    r = requests.get(w.image, stream=True)
                    bucket.upload_fileobj(
                        r.raw, (w.name+'_'+a.last_name).replace(' ', '_')+'.jpg')
                    Work(artist=a, name=w.name, start_year=w.start_year, finish_year=w.finish_year,
                         info=w.info, location=w.location, image=w.image).save()
                except Exception as e:
                    print(e)

                print(w.name + ' is inserted / artist id = ' + str(a.id))
