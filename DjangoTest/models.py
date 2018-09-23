from django.db import models


class Blogger(models.Model):
    nick = models.CharField(max_length=12, null=False, unique=True)
    reputation = models.FloatField(default=0.0, null=False)
    registration_date = models.DateField(null=False)
    subscribers_count = models.IntegerField(default=0, null=False)
    profit = models.FloatField(default=0.0, null=False)

    class Meta:
        db_table = 'blogger'


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
