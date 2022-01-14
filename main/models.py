import os.path

from django.db import models
from django.contrib.auth.models import User


def get_path(instance, filename):
    return '{0}/{1}'.format(instance.author.username, filename)


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateTimeField(default='2000-01-01 00:00')
    title = models.CharField(max_length=80, default='')
    image = models.ImageField(upload_to=get_path, blank=True)
    text = models.TextField(blank=True)

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    add_date = models.DateTimeField(default='')
    text = models.TextField(default='')


class Friend(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person')
    whom = models.ForeignKey(User, on_delete=models.CASCADE)


class Auth(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.TextField(unique=True)
