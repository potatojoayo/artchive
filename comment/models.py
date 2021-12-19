from django.db import models
from user.models import User
from work.models import Work
from artist.models import Artist

# Create your models here.


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    work_id = models.ForeignKey(
        Work, on_delete=models.CASCADE, null=True, blank=True)
    artist_id = models.ForeignKey(
        Artist, on_delete=models.CASCADE, null=True, blank=True)
    contents = models.CharField(max_length=255, null=False)
    # Comment 테이블을 참조 (self reference field)
    replying_comment_id = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
