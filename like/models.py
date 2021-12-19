from django.db import models
from user.models import User
from artist.models import Artist
from work.models import Work
from comment.models import Comment

# Create your models here.


class Like(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    artist_id = models.ForeignKey(
        Artist, on_delete=models.CASCADE, null=True, blank=True)
    work_id = models.ForeignKey(
        Work, on_delete=models.CASCADE, null=True, blank=True)
    comment_id = models.ForeignKey(
        Comment, on_delete=models.CASCADE, null=True, blank=True)
