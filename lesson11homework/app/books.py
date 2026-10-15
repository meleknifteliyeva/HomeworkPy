from .validation import validate_title, validate_author, validate_year

books = []


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
    print(f"{book['title']} kitabi silindi.")