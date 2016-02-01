from django.contrib.auth.models import User
from rest_framework import serializers
from dailyhn.models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        # fields = ('id', 'author', 'text', 'created', 'updated')
        fields = ('url', 'date', 'points', 'title', 'article_url', 'comment_url', 'created', 'updated')


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

