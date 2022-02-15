from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
class User(AbstractUser):
    pass

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=160, default=None)
    content = models.TextField()
    timestamp = models.DateTimeField(default=datetime.datetime.now)