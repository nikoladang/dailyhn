from django.db import models
from django.contrib.auth.models import User


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


class Bookmark(models.Model):
    user = models.ManyToManyField(User, default="nikola", editable=False)
    entry = models.ManyToManyField(Entry)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

# class UserProfile():
#     user = models.OneToOneField(User, related_name='profile')
#
#     def __str__(self):
#         return "{0}'s profile".format(self.user.username)
#
#     class Meta:
#         db_table = 'user_profile'


# # Create your models here.
# class SavedEmbed(models.Model):
#     type = models.CharField(max_length=15)
#     provider_url = models.URLField()
#     provider_name = models.CharField(max_length=100)
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     html = models.TextField()
#     width = models.IntegerField()
#     height = models.IntegerField()
#     thumbnail_url = models.URLField()
#     thumbnail_width = models.IntegerField()
#     thumbnail_height = models.IntegerField()
#     author_url = models.URLField()
#     author_name = models.CharField(max_length=100)
#     version = models.DecimalField(max_digits=4, decimal_places=2)