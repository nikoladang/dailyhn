from django.contrib import admin

# Register your models here.
from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ["date", "points", "title", "url", "n_bookmarks"]
    class Meta:
        model = Entry


admin.site.register(Entry, EntryAdmin)