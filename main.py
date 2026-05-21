import json


class Book:

    def __init__(self, title, author):

        self.title = title
        self.author = author

    def __str__(self):

        return f"{self.title} by {self.author}"

    def to_dict(self):

        return {
            "title": self.title,
            "author": self.author
        }

    def display_book(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = Book(title, author)
        self.books.append(book)

        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books found.")
            return

        print("\nBook List:")

        for index, book in enumerate(self.books, start=1):
            print(f"\nBook {index}")
            book.display_book()

    def save_books(self):
        data = []

        for book in self.books:
            data.append({
                "title": book.title,
                "author": book.author
            })

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Books saved successfully!")

    def load_books(self):
        try:
            with open("books.json", "r") as file:
                data = json.load(file)

                for item in data:
                    book = Book(item["title"], item["author"])
                    self.books.append(book)

        except FileNotFoundError:
            print("No previous books found.")


def main():

    manager = BookManager()

    manager.load_books()

    while True:

        print("\n===== BOOK MANAGER =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Save Books")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_book()

        elif choice == "2":
            manager.view_books()

        elif choice == "3":
            manager.save_books()

        elif choice == "4":
            manager.save_books()
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()