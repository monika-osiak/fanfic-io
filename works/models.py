from django.db import models
from django.utils import timezone


class Story(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    created_date = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Stories"


class Chapter(models.Model):
    of_story = models.ForeignKey(Story, on_delete=models.CASCADE)
    number = models.IntegerField()
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)
    content = models.TextField()


class Character(models.Model):
    name = models.CharField(max_length=100)
    of_story = models.ForeignKey(Story, on_delete=models.CASCADE)
