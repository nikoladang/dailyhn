from django.contrib import admin
from .models import Entry, Bookmark


class EntryAdmin(admin.ModelAdmin):
    list_display = ["date", "points", "title", "url", "n_bookmarks"]
    class Meta:
        model = Entry


admin.site.register(Entry, EntryAdmin)
admin.site.register(Bookmark)

# class EntryAdmin(admin.ModelAdmin):
#     list_display = ["date", "points", "title", "url", "n_bookmarks"]
#     class Meta:
#         model = SavedEmbed


# admin.site.register(SavedEmbed, EntryAdmin)

# Register your models here.