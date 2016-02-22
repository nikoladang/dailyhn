from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    date = models.DateField() # datetime.date instance
    points = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    article_url = models.URLField()
    comment_url = models.URLField()
    n_bookmarks = models.IntegerField(verbose_name="Bookmarks", default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.date) + "|" + str(self.points) + "|" + self.title

    class Meta:
        verbose_name_plural = "Entries"
        unique_together = ('date', 'title')


class Bookmark(models.Model):
    # user = models.ManyToManyField(User, default="nikola", editable=False)
    # entry = models.ManyToManyField(Entry)
    # user = models.ForeignKey(User)
    entry = models.ForeignKey(Entry, null=True)
    star = models.NullBooleanField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        # bookmark = Bookmark.objects.get(pk=1)
        return str(self.entry)

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