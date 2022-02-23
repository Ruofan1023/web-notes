from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

from numpy import array

# Create your models here.
class User(AbstractUser):
    pass


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=160, default=None)
    content = models.TextField()
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    isarchive = models.BooleanField(default=False)


class PinQueue(models.Model):
    queue = models.JSONField(default="")

    def __str__(self):
        return str(self.queue)
