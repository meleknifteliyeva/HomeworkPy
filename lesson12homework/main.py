from app.config import BOOKS_FILE
from app.books import (
    books,
    load_saved_books,
    add_book,
    show_books,
    find_book_by_title,
    find_books_by_author,
    delete_book,
    format_book,
)
from app.reports import create_report, read_report


def search_by_title(title):
    book = find_book_by_title(title)
    if book is None:
        print("Kitab tapilmadi.")
    else:
        print(format_book(book))


def search_by_author(author):
    author_books = find_books_by_author(author)
    if len(author_books) == 0:
        print("Bu muellife aid kitab tapilmadi.")
    else:
        for book in author_books:
            print(format_book(book))


def run_first():
    print("=== BIRINCI RUN ===")

    # Test kitablari yalniz fayl yoxdursa elave olunur
    if not BOOKS_FILE.exists():
        add_book("1984", "George Orwell", 1949)
        add_book("Animal Farm", "George Orwell", 1945)
        add_book("The Hobbit", "J.R.R. Tolkien", 1937)
        add_book("Clean Code", "Robert C. Martin", 2008)
        add_book("Python Crash Course", "Eric Matthes", 2015)
        add_book("A", "", 3000)  # duzgun deyil
    else:
        print("books.json artiq var, kitablar yeniden elave edilmir.")

    show_books()
    create_report(books)


def run_second():
    print("=== IKINCI RUN ===")
    print(f"Fayldan berpa olunan kitab sayi: {len(books)}")

    print("\n--- Kitab adina gore axtaris ---")
    search_by_title("The Hobbit")

    print("\n--- Muellife gore axtaris ---")
    search_by_author("George Orwell")

    print("\n--- Kitab silinir ---")
    delete_book("1984")


def run_third():
    print("=== UCUNCU RUN ===")
    print(f"Fayldan berpa olunan kitab sayi: {len(books)}")

    print("\n--- Silinmis kitab axtarilir ---")
    search_by_title("1984")

    print("\n--- Hesabat yenilenir ---")
    create_report(books)

    print("\n--- Hesabat fayldan oxunur ---")
    content = read_report()
    if content is None:
        print("Hesabat hele yaradilmayib.")
    else:
        print(content)


def main():
    # Proqram baslayanda kitablar fayldan oxunur
    load_saved_books()

    print("1 - Birinci run")
    print("2 - Ikinci run")
    print("3 - Ucuncu run")
    choice = input("Secim: ")

    if choice == "1":
        run_first()
    elif choice == "2":
        run_second()
    elif choice == "3":
        run_third()
    else:
        print("Yanlis secim")


if __name__ == "__main__":
    main()