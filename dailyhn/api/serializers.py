from rest_framework import serializers
from dailyhn.models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        # fields = ('id', 'author', 'text', 'created', 'updated')
        fields = ('url', 'date', 'points', 'title', 'article_url', 'comment_url', 'created', 'updated')