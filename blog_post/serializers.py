from rest_framework import serializers
from .models import BlogPostModel, Comment
from django.contrib.auth.models import User


class PostListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = BlogPostModel
        fields = ['id', 'title', 'description', 'owner', 'comments']


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
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'post']

