from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='users_pictures',
                                blank=True,
                                default='empty.jpg')
