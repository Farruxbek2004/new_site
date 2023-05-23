from django.db import models
import random
from django.utils.text import slugify


class BlogPostModel(models.Model):
    """
    Blogpost Model
    """
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/', blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        slug = self.slug
        while self.__class__.objects.filter(slug=slug).exists():
            slug = f"{self.slug}-{random.randint(1, 100000)}"
        self.slug = slug
        return super().save(*args, **kwargs)

    @property
    def likes(self):
        return self.like_dislike.filter(type=LikeDislike.LikeDislikeType.LIKE).count()

    @property
    def dislikes(self):
        return self.like_dislike.filter(type=LikeDislike.LikeDislikeType.DISLIKE).count()


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey('BlogPostModel', on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies", null=True)
    class Meta:
        ordering = ['created_at']


class LikeDislike(models.Model):
    class LikeDislikeType(models.IntegerChoices):
        LIKE = 1
        DISLIKE = -1

    post = models.ForeignKey("BlogPostModel", on_delete=models.CASCADE, related_name="like_dislike")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="like_dislike")
    type = models.SmallIntegerField(choices=LikeDislikeType.choices)

    class Mete:
        unique_together = ["post", "user"]

    def __str__(self):
        return str(self.user)
