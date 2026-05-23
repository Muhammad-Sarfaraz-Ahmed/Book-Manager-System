from main import Book, BookManager


def test_book_title():

    book = Book("Python", "Ali")

    assert book.title == "Python"


def test_book_author():

    book = Book("Python", "Ali")

    assert book.author == "Ali"

def test_empty_book_list():

    manager = BookManager()

    assert manager.books == []