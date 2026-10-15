def validate_title(title):
    return len(title.strip()) >= 2


def validate_author(author):
    return len(author.strip()) >= 2


def validate_year(year):
    return year > 0 and year <= 2026