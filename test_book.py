from main import Book


def test_book_title():

    book = Book("Python", "Ali")

    assert book.title == "Python"


def test_book_author():

    book = Book("Python", "Ali")

    assert book.author == "Ali"