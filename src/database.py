import threading
from datetime import datetime, timedelta

class Database:
    def __init__(self):
        self.data = {}
        self.lock = threading.Lock()
    
    def add(self, key: str, status: int) -> None:
        with self.lock:
            self.data[key] = {'status': status, 'date': datetime.now()}
    
    def update(self, key: str, status: int) -> None:
        with self.lock:
            self.data[key]['status'] = status
            self.data[key]['date'] = datetime.now()
    
    def get(self, key: str) -> dict:
        x = None
        with self.lock:
            x = self.data[key]
        return x
    
    def get_status(self, key: str) -> int:
        x = None
        with self.lock:
            x = self.data[key]['status']
        return x
    
    def get_date(self, key: str) -> datetime:
        x = None
        with self.lock:
            x = self.data[key]['date']
        return x