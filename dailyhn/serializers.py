from rest_framework import serializers
from .models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        # fields = ('id', 'author', 'text', 'created', 'updated')
        fields = ('date', 'points', 'title', 'article_url', 'comment_url', 'created', 'updated')