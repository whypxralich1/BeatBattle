from django.db import models

class Track(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)