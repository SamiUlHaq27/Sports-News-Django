from django.db import models
from datetime import datetime


# Create your models here.

class New(models.Model):
    rank = models.IntegerField()
    title = models.TextField()
    publish_date = models.CharField(max_length=50)
    our_category = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField()
    thumbnail = models.URLField()
    media = models.URLField()
    link = models.URLField()
    blog_url = models.TextField()

class Blog(models.Model):
    rank = models.IntegerField()
    title = models.TextField()
    publish_date = models.CharField(max_length=50)
    our_category = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField()
    thumbnail = models.URLField()
    media = models.URLField()
    link = models.URLField()
    blog_url = models.TextField()

class Refresh(models.Model):
    name = models.CharField(max_length=50)
    time = models.CharField(max_length=100)

class Comment(models.Model):
    profile_picture = models.ImageField(upload_to="comments/",default="err.png")
    text = models.TextField()
    name = models.CharField(max_length=60)
    email = models.EmailField()
    website = models.URLField()
    date = models.DateTimeField(default=datetime.now)


