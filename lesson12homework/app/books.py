from .validation import validate_title, validate_author, validate_year
from .storage import save_books, load_books
from .history import write_history

books = []


def load_saved_books():
    loaded_books = load_books()
    books.clear()
    books.extend(loaded_books)


def add_book(title, author, year):
    if not validate_title(title):
        print("Kitabin adi duzgun deyil")
        return
    if not validate_author(author):
        print("Muellif duzgun deyil")
        return
    if not validate_year(year):
        print("Il duzgun deyil")
        return

    book = {
        "title": title.strip(),
        "author": author.strip(),
        "year": year
    }

    books.append(book)
    save_books(books)
    write_history("ELAVE EDILDI", book["title"])


def format_book(book):
    return f"{book['title']} | {book['author']} | {book['year']}"


def show_books():
    if len(books) == 0:
        print("Sistemde kitab yoxdur")
        return

    for book in books:
        print(format_book(book))


def find_book_by_title(title):
    for book in books:
        if book["title"].lower() == title.strip().lower():
            return book
    return None


def find_books_by_author(author):
    result = []
    for book in books:
        if book["author"].lower() == author.strip().lower():
            result.append(book)
    return result


def delete_book(title):
    book = find_book_by_title(title)
    if book is None:
        print("Kitab tapilmadi.")
        return

    books.remove(book)
    save_books(books)
    write_history("SILINDI", book["title"])
    print(f"{book['title']} kitabi silindi.")