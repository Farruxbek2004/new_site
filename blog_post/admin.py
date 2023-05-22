from django.contrib import admin
from .models import BlogPostModel, Comment

admin.site.register(BlogPostModel)
admin.site.register(Comment)
