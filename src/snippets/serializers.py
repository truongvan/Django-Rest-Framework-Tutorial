from rest_framework import serializers
from .models import Snippet, LANGUAGES_CHOICES, STYLE_CHOICES


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     lineos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGES_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         return Snippets.object.create(**validated_data)

    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.title)
#         instance.language= validated_data.get('language', instance.title)
#         instance.style = validated_data.get('style', instance.title)
#         instance.lineos = validated_data.get('lineos', instance.title)
#         instance.save()
#         return instance

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'created', 'title', 'code', 'lineos', 'language', 'style')