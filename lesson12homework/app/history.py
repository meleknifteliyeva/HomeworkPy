from datetime import datetime
from .config import HISTORY_FILE


def write_history(operation, title):
    operation_time = datetime.now().isoformat(timespec="seconds")

    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"{operation_time} | {operation} | {title}\n")