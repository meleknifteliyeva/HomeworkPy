from app.books import (
    books,
    add_book,
    show_books,
    find_book_by_title,
    find_books_by_author,
    delete_book,
    format_book,
)
from app.book_stats import get_total_count, get_old_books_count, get_average_year


def main():
    add_book("1984", "George Orwell", 1949)
    add_book("Animal Farm", "George Orwell", 1945)
    add_book("The Hobbit", "J.R.R. Tolkien", 1937)
    add_book("Clean Code", "Robert C. Martin", 2008)
    add_book("Python Crash Course", "Eric Matthes", 2015)
    add_book("A", "", 3000)

    print("\n--- Butun kitablar ---")
    show_books()

    print("\n--- Kitab adina gore axtaris ---")
    book = find_book_by_title("1984")
    if book is None:
        print("Kitab tapilmadi.")
    else:
        print(format_book(book))

    print("\n--- Muellife gore axtaris ---")
    author_books = find_books_by_author("George Orwell")
    if len(author_books) == 0:
        print("Bu muellife aid kitab tapilmadi.")
    else:
        for item in author_books:
            print(format_book(item))

    print("\n--- Statistika ---")
    print(f"Umumi kitab sayi: {get_total_count(books)}")
    print(f"2000-ci ilden evvel cixan kitablarin sayi: {get_old_books_count(books)}")
    print(f"Orta buraxilis ili: {get_average_year(books)}")

    print("\n--- Kitab silinir ---")
    delete_book("1984")

    print("\n--- Silinenden sonra ---")
    show_books()
    if find_book_by_title("1984") is None:
        print("1984 artiq siyahida yoxdur.")


if __name__ == "__main__":
    main()