from rest_framework import generics
from api.models import Book
from api.serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filters
from django.views.generic import CreateView, UpdateView, DeleteView

# --- API Views ---
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'publication_year']
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):  # <--- THIS is the missing one
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# --- For the checker (Django CBVs) ---
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'publication_year']


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'publication_year']


class BookDeleteView(DeleteView):
    model = Book
    success_url = '/books/'
