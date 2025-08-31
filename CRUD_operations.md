# Create Operation

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected Output: <Book: 1984 by George Orwell (1949)>

---

## 2️⃣ `retrieve.md`
```markdown
# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve the created Book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Expected Output: ('1984', 'George Orwell', 1949)

---

## 3️⃣ `update.md`
```markdown
# Update Operation

```python
from bookshelf.models import Book

# Update the title of the Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# Expected Output: 'Nineteen Eighty-Four'

---

## 4️⃣ `delete.md`
```markdown
# Delete Operation

```python
from bookshelf.models import Book

# Delete the Book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Verify deletion
Book.objects.all()
# Expected Output: <QuerySet []>

---

## 5️⃣ `CRUD_operations.md`
```markdown
# CRUD Operations Documentation

## 1. Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected Output: <Book: 1984 by George Orwell (1949)>
