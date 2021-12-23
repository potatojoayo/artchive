from django.db import models
from artist.models import Artist

# Create your models here.


class Work(models.Model):

    # 1:N 관계의 relation (work = 1, artist = n)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='works')
    name = models.CharField(max_length=255, null=False)
    start_year = models.IntegerField(null=True, blank=True)
    finish_year = models.IntegerField(null=True, blank=True)
    info = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.CharField(max_length=255, null=False)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

    class Meta:
        unique_together = ['artist', 'name', 'info']
