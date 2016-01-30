# from django.shortcuts import render
from django.views.generic import ListView
from dailyhn.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    template_name = "bookmark/bookmark_list.html"

    def get_context_data(self, **kwargs):
        context = super(BookmarkListView, self).get_context_data(**kwargs)
        print(context)
        context["queryset"] = Bookmark.objects.all()
        return context

