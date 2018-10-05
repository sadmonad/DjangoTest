from django.db import models
from ..bloggers.models import Blogger


class Video(models.Model):
    caption = models.CharField(max_length=30, null=False)
    uploading_date = models.DateTimeField(null=False)
    duration_min = models.FloatField(null=False)
    genre = models.CharField(max_length=10, null=False)
    views_count = models.PositiveIntegerField(default=0, null=False)
    likes_count = models.PositiveIntegerField(default=0, null=False)
    comments_count = models.PositiveIntegerField(default=0, null=False)
    is_private = models.BooleanField(default=False, null=False)
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)

    class Meta:
        db_table = 'video'
