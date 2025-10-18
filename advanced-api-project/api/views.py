from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Book
from api.serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Add filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filter by these fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Searchable fields (use ?search=)
    search_fields = ['title', 'author__name']

    # Orderable fields (use ?ordering=title or ?ordering=-publication_year)
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']
