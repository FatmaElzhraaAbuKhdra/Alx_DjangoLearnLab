# Delete the Book instance

```python
from bookshelf.models import Book

# Retrieve and delete the specific book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Verify that the book no longer exists in the database
Book.objects.all()
# Expected Output: QuerySet([])
```
