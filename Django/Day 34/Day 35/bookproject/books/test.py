from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Book


class BookAPITest(APITestCase):


 def setUp(self):
  self.admin = User.objects.create_superuser('admin', 'a@test.com', 'pass123')
  self.user = User.objects.create_user('user', 'u@test.com', 'pass123')
  self.book = Book.objects.create(title='Django', author='Author', published_date='2024-01-01')


def test_get_books(self):
 self.client.login(username='user', password='pass123')
 response = self.client.get('/api/books/')
 self.assertEqual(response.status_code, status.HTTP_200_OK)


def test_create_book(self):
   self.client.login(username='user', password='pass123')
   data = {'title':'API Book','author':'Test','published_date':'2024-01-01'}
   response = self.client.post('/api/books/', data)
   self.assertEqual(response.status_code, status.HTTP_201_CREATED)

def test_update_book(self):
  self.client.login(username='user', password='pass123')
  data = {'title':'Updated','author':'New','published_date':'2024-01-02'}
  response = self.client.put(f'/api/books/{self.book.id}/', data)
  self.assertEqual(response.status_code, status.HTTP_200_OK)


def test_delete_book_admin_only(self):
  self.client.login(username='admin', password='pass123')
  response = self.client.delete(f'/api/books/{self.book.id}/')
  self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


def test_unauthenticated_access(self):
 response = self.client.get('/api/books/')
 self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)