from django.db import models
from entry.models import Entry

# Create your models here.

class Bookmark(models.Model):
    # user = models.ManyToManyField()
    entry = models.ManyToManyField(Entry)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

