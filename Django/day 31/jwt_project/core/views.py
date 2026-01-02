from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Post
from .serializers import PostSerializer

# API for all authenticated users
class PostListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


# API only for Admin users
class PostCreateAPI(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# Frontend Views
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def add_post(request):
    if request.method == 'POST':
        Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('/')