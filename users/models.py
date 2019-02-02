from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class UserProfile():
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    description = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='users_pictures',
                                blank=True,
                                default='empty.jpg')
