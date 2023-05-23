from rest_framework import serializers
from .models import BlogPostModel, Comment, LikeDislike
from django.contrib.auth.models import User


class PostListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = BlogPostModel
        fields = ['id', 'title', 'description', 'owner', 'comments', 'likes', 'dislikes']


class PostCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        model = BlogPostModel
        fields = ["id", "title", "slug", 'description']


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'description', 'owner', 'post']


class LikeDislikeSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=LikeDislike.LikeDislikeType.choices)

    class Mete:
        model = LikeDislike
        fields = ["id", "post", "user", "type"]

    #
    #
    # class UserSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = User
    #         fields = ['id', 'username', 'post']
