from django.contrib import admin
from .models import Blog, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Blog, BlogAdmin)
