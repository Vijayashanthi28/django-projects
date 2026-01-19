from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly


class BookListCreateView(generics.ListCreateAPIView):
 queryset = Book.objects.all()
serializer_class = BookSerializer
permission_classes = [IsAuthenticated]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
 queryset = Book.objects.all()
serializer_class = BookSerializer
permission_classes = [IsAdminOrReadOnly]