import json
from .config import BOOKS_FILE


def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def load_books():
    if not BOOKS_FILE.exists():
        return []

    with open(BOOKS_FILE, "r", encoding="utf-8") as file:
        loaded_books = json.load(file)
    return loaded_books