import json
from config.constants import HISTORY_LIMIT

class HistoryManager:
    def __init__(self):
        self.history = []

    def add(self, record: str):
        self.history.append(record)
        if len(self.history) > HISTORY_LIMIT:
            self.history.pop(0)

    def get_all(self) -> list:
        return self.history.copy()

    def save_to_file(self):
        with open("history.json", "w") as f:
            json.dump(self.history, f)

    def load_from_file(self):
        try:
            with open("history.json", "r") as f:
                self.history = json.load(f)
        except FileNotFoundError:
            pass