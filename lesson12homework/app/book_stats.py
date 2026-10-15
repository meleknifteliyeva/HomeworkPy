def get_total_count(books):
    return len(books)


def get_old_books_count(books):
    count = 0
    for book in books:
        if book["year"] < 2000:
            count += 1
    return count


def get_average_year(books):
    if len(books) == 0:
        return 0

    total = 0
    for book in books:
        total += book["year"]
    return round(total / len(books), 1)