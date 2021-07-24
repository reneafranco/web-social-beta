from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField

from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    content = models.TextField()
    created_at = DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=200, verbose_name="comment")
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True, verbose_name="Nombre")
    location = models.CharField(max_length=100, null=True)
    web = models.CharField(max_length=200, null=True, verbose_name="WEBSITE")
    picture = models.ImageField(upload_to='uploads/profile_pictures/', default='uploads/profile_pictures/default.png',
                                null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True),






