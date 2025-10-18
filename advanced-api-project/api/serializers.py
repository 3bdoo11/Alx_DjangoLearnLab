from rest_framework import serializers
from api.models import Author
from api.models import Book
from datetime import date


# Serializer for the Book model
# Includes custom validation to ensure publication_year is not in the future
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for the Author model
# Includes nested BookSerializer to show all books by that author
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
