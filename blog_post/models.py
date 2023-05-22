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


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey('BlogPostModel', on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies')

    class Meta:
        ordering = ['created_at']
# class CourseContent(AbstractUser):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     video = models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
#     time = models.TimeField(auto_now_add=True)
#     position = models.IntegerField()
#     is_public = models.BooleanField()
#     course_id = models.ForeignKey(on_delete=models.CASCADE, related_name='course_content')
#
#     def __str__(self):
#         return self.title
# class Rate(models.Choices):
#     CHOICE_ONE = 1
#     CHOICE_TWO = 2
#     CHOICE_THREE = 3
#     CHOICE_FOUR = 4
#     CHOICE_FIVE = 5
# class Review(models.Model):
#     user = models.ForeignKey(
#         "users.User",
#         on_delete=models.CASCADE,
#         related_name="user"
#     )
#     course = models.ForeignKey(
#         Course,
#         on_delete=models.CASCADE,
#         related_name="course"
#     )
#     rate = models.PositiveIntegerField(max_length=20, choices=Rate.choices)
#     comment = models.CharField(max_length=400)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return str(self.user)