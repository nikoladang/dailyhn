from django.db import models

# Create your models here.

class Entry(models.Model):
    date = models.CharField()
    title = models.CharField()
    url = models.URLField()
    bookmarks = models.
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)