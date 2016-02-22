from django.contrib import admin
from .models import Entry, Bookmark


admin.site.site_header = "DailyHackerNews administration"
admin.site.site_title = "DailyHackerNews site admin"

class EntryAdmin(admin.ModelAdmin):
    list_display = ["date", "points", "title", "article_url", "comment_url", "n_bookmarks","created","updated"]
    list_display_links = ["title"]
    ordering = ["-date","-points"]
    readonly_fields = ['points','n_bookmarks']
    class Meta:
        model = Entry

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ["__str__", "entry","created"]
    class Meta:
        model = Bookmark



admin.site.register(Entry, EntryAdmin)
admin.site.register(Bookmark, BookmarkAdmin)

# class EntryAdmin(admin.ModelAdmin):
#     list_display = ["date", "points", "title", "url", "n_bookmarks"]
#     class Meta:
#         model = SavedEmbed


# admin.site.register(SavedEmbed, EntryAdmin)

# Register your models here.