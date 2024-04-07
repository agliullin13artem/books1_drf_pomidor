
from rest_framework.viewsets import ModelViewSet
import django_filters.rest_framework
from rest_framework.filters import SearchFilter, OrderingFilter


from .models import Book
from .serializers import BooksSerializer

class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_fields = ['price', 'author_name']
