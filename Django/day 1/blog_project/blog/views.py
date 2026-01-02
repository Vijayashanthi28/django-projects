from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost
from .serializers import BlogPostSerializer
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

def test_view(request):
    """Simple test view"""
    return render(request, 'blog/test.html')

def home(request):
    """Home page view"""
    return render(request, 'blog/index.html')

# API Views
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_queryset(self):
        return BlogPost.objects.all().order_by('-published_date')

# Template-based Views
class PostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})
    
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
    
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

# Home view
def home(request):
    return render(request, 'blog/index.html')