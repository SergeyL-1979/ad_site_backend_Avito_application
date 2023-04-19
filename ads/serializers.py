from rest_framework import serializers

from ads.models import Comment, Ad


# Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    ad = serializers.SlugRelatedField(read_only=True, slug_field="title")
    author = serializers.SlugRelatedField(read_only=True, slug_field="first_name", )

    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="first_name", )

    class Meta:
        model = Ad
        fields = ["author", "title", "price", "description", "image", "created_at", ]


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
