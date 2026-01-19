from rest_framework.viewsets import ModelViewSet
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from django.shortcuts import render

# -------- API VIEWSETS --------

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()  
    serializer_class = BookSerializer

    def get_queryset(self):
        genre = self.request.query_params.get('genre')
        author_id = self.request.query_params.get('author')

        queryset = Book.objects.all()

        if genre:
            queryset = queryset.filter(genre__iexact=genre)
        if author_id:
            queryset = queryset.filter(author_id=author_id)

        return queryset


# -------- FRONTEND VIEWS --------

def authors_page(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})


def books_page(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'books.html', {'books': books})
