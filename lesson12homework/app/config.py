from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

BOOKS_FILE = DATA_DIR / "books.json"
REPORT_FILE = DATA_DIR / "report.txt"
HISTORY_FILE = DATA_DIR / "history.txt"