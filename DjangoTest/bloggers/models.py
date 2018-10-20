from django.db import models
from ..accounts.profile.models import Profile


class Blogger(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    nick = models.CharField(max_length=12, null=False, unique=True)
    reputation = models.FloatField(default=0.0, null=False)
    registration_date = models.DateField(null=False)
    subscribers_count = models.IntegerField(default=0, null=False)
    profit = models.FloatField(default=0.0, null=False)

    class Meta:
        db_table = 'blogger'
