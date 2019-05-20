from rest_framework import serializers
from .models import Snippet, LANGUAGES_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'created', 'title', 'code', 'linenos', 'language', 'style')