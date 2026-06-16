from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Track(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField(upload_to='tracks/', blank=True, null=True, verbose_name='Обложка')
    tags = models.ManyToManyField(Tag, blank=True, related_name='tracks', verbose_name='Теги')

    def __str__(self):
        return f"{self.artist} - {self.title}"