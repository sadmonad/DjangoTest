from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_blogger = models.BooleanField(default=False)
    is_advertiser = models.BooleanField(default=False)
    is_regular_user = models.BooleanField(default=False)

    class Meta:
        db_table = 'profile'
