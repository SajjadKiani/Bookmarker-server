from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Bookmarks(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=300)
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    favicon = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
