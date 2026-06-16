from django.db import models
from django.contrib.auth.models import User

class Track(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')