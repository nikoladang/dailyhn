from django.db import models

# Create your models here.

class Bookmark(models.Model):
    date = models.CharField()
    title = models.CharField()
    url = models.URLField()
