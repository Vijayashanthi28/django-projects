from rest_framework import serializers
from .models import BlogPost
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), 
        write_only=True,
        source='author'
    )
    
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'author_id', 'published_date', 'updated_date']
        read_only_fields = ['published_date', 'updated_date']