from django.contrib import admin

from .models import Post, FeaturedPost, Comment


# Register your models here.
admin.site.register(Post)
admin.site.register(FeaturedPost)
admin.site.register(Comment)
