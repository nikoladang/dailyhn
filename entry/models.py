from django.db import models


# Create your models here.

class Entry(models.Model):
    date = models.DateField()
    points = models.IntegerField()
    title = models.CharField(max_length=255)
    url = models.URLField()
    n_bookmarks = models.IntegerField(verbose_name="Bookmarks")
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.date) + "|" + str(self.points) + "|" + self.title

    class Meta:
        verbose_name_plural = "Entries"

