from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

from rest_framework import viewsets
from .serializers import BlogPostSerializer
from .permissions import IsOwnerOrReadOnly

# FRONTEND VIEWS
def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = BlogPost.objects.get(id=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'blog/post_form.html', {'form': form})

# API VIEW
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsOwnerOrReadOnly]
