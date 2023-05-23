from django.contrib import admin
from .models import BlogPostModel, Comment, LikeDislike


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["created_at", "body", "owner", "post"]


admin.site.register(BlogPostModel)
admin.site.register(LikeDislike)
