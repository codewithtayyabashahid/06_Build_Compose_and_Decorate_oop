class Book:
    total_books = 0 
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# usage
book1 = Book("1984", "George Orwell")
book2 = Book("Pride and Prejudice", "Jane Austen")
print(Book.total_books)  