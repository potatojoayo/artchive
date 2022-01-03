from django.core.management.base import BaseCommand
from work.models import Work
import requests
import boto3
from ._get_image_size import get_size


class Command(BaseCommand):

    help = 'upload image from url to s3'

    def handle(self, *args, **options):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket('artchivepotatojoayo')
        works = Work.objects.filter(width=0, height=0)
        for i, w in enumerate(works):
            r = requests.get(w.image, stream=True)
            width, height = 0, 0
            try:
                width, height = get_size(w.image)
                w.width = width
                w.height = height
            except Exception as e:
                print(e)
            w.save()
            bucket.upload_fileobj(
                r.raw, (w.name+'_'+w.artist.last_name).replace(' ', '_')+'.jpg')
            print('{} / {}, width={} height={} was uploaded completely. {} / {}'.format(w.name,
                  w.artist.last_name, width, height, i, len(works)))
            r.close()
