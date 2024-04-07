from urllib import response
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from store.models import Book
from store.serializers import BooksSerializer


class BookApiTestCase(APITestCase):
    def setUp(self):
        self.book_1 = Book.objects.create(
            name="Test_book1", price=25, author_name="Test"
        )
        self.book_2 = Book.objects.create(
            name="Test_book2", price=55, author_name="Author 1"
        )
        self.book_3 = Book.objects.create(
            name="Test_book3", price=55, author_name="Author 2"
        )

    def test_get(self):
        url = reverse("book-list")
        response = self.client.get(url)
        serializer_data = BooksSerializer([self.book_1, self.book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


    def test_get_filter(self):
        url = reverse("book-list")
        response = self.client.get(url)
        serializer_data = BooksSerializer([self.book_1, self.book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
