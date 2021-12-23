from django.core.management.base import BaseCommand
from work.models import Work
import requests
import boto3


class Command(BaseCommand):

    help = 'upload image from url to s3'

    def handle(self, *args, **options):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket('artchivepotatojoayo')
        works = Work.objects.filter(id__gte=2136)
        for i, w in enumerate(works):
            r = requests.get(w.image, stream=True)
            bucket.upload_fileobj(
                r.raw, (w.name+'_'+w.artist.last_name).replace(' ', '_')+'.jpg')
            print('{} / {} was uploaded completely. {} / {}'.format(w.name,
                  w.artist.last_name, i, len(works)))
