from django.db import models
from django.contrib.auth.models import User


def get_path(instance, filename):
    pass
    return '{0}/{1}'.format(instance)

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateTimeField(default='')
    title = models.CharField(max_length=80, default='')
    #image = models.ImageField(upload_to='file')
    text = models.TextField(blank=True)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    add_date = models.DateTimeField(default='')
    text = models.TextField(default='')


class Friend(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE, related_name='person')
    whom = models.ForeignKey(User, on_delete=models.CASCADE)
