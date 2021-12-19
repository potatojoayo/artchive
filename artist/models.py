from django.db import models

# Create your models here.


class Artist(models.Model):

    last_name = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    born = models.IntegerField(blank=True, null=True)
    died = models.IntegerField(blank=True, null=True)
    period = models.CharField(max_length=20, blank=True, null=True)
    profession = models.CharField(max_length=20, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ('last_name',  'nationality',
                           'died', 'period', 'profession')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
