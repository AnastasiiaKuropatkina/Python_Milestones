class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category


class Shelf:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def sort_books(self):
        self.books.sort(key=lambda book: book.title)


class Room:
    def __init__(self):
        self.shelves = {}

    def organize_books(self, books):
        for book in books:
            if book.category not in self.shelves:
                self.shelves[book.category] = Shelf()
            self.shelves[book.category].add_book(book)

    def sort_shelves(self):
        for shelf in self.shelves.values():
            shelf.sort_books()


books = {
    Book("The Grass is Always Greener", "Jeffrey Archer", "Modern Times"),
    Book("The Higgler", "A. E. Coppard ", "Romance"),
    Book("The Open Boat", "Stephen Crane", "Classic"),
    Book("The Speckled Band", "Sir Arthur Conan Doyle", "Crime")
}


bob_room = Room()
bob_room.organize_books(books)
bob_room.sort_shelves()


for category, shelf in bob_room.shelves.items():
    print(f"Category: {category}")
    for book in shelf.books:
        print(f" - {book.title} by {book.author}")