# Delete Operation

```python
from bookshelf.models import Book

# Delete the Book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Verify deletion
Book.objects.all()
# Expected Output: <QuerySet []>
