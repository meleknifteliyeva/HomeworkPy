from .config import REPORT_FILE
from .books import format_book
from .book_stats import get_total_count, get_old_books_count, get_average_year


def create_report(books):
    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        file.write("--- Kitab siyahisi ---\n")

        if len(books) == 0:
            file.write("Sistemde kitab yoxdur.\n")
        else:
            for book in books:
                file.write(format_book(book) + "\n")

        file.write("\n")
        file.write(f"Umumi kitab sayi: {get_total_count(books)}\n")
        file.write(f"2000-ci ilden evvel cixan kitablarin sayi: {get_old_books_count(books)}\n")
        file.write(f"Orta buraxilis ili: {get_average_year(books)}\n")

    print("Hesabat yaradildi.")


def read_report():
    if not REPORT_FILE.exists():
        return None

    with open(REPORT_FILE, "r", encoding="utf-8") as file:
        content = file.read()
    return content