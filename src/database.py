import threading, copy, os
import dill
from datetime import datetime

import hb

class Database:
    def __init__(self, accessories: list) -> None:
        self.data = {}
        self.lock = threading.Lock()
        try:
            for accessory in accessories:
                accessory_values = hb.get_accessory_characteristics(accessory['uniqueId'])
                self.add(accessory['uniqueId'], accessory_values, accessory['serviceName'])
        except Exception as e:
            raise Exception(str(e))
    
    def __str__(self) -> str:
        text = ""
        for accessory in self.data:
            text = text + accessory + ":\n" + str(self.get_accessory_data(accessory)) + "\n\n"
        return text[:-1]
        
    def add(self, key: str, values: dict, name: str = None) -> None:
        with self.lock:
            if name != None:
                self.data[key] = {'values': values, 'serviceName': name, 'date': datetime.now()}
            else:
                self.data[key] = {'values': values, 'serviceName': self.data[key]['serviceName'], 'date': datetime.now()}
    
    def update_accessories_values(self) -> None:
        try:
            for accessory in self.data:
                accessory_values = hb.get_accessory_characteristics(accessory)
                if self.get_accessory_values(accessory) == accessory_values:
                    return
                self.add(accessory, accessory_values)
        except Exception as e:
            raise Exception(str(e))
    
    def update_accessory_values(self, key: str) -> None:
        try:
            accessory_values = hb.get_accessory_characteristics(key)
            if self.get_accessory_values(key) == accessory_values:
                return
            self.add(key, accessory_values)
        except Exception as e:
            raise Exception(str(e))
    
    def update_accessory_value(self, key: str, characteristicType: str) -> None:
        try:
            accessory_value = hb.get_accessory_characteristic(key, characteristicType)
            accessory_values = copy.copy(self.get_accessory_values(key))
            accessory_values[characteristicType] = accessory_value
            if self.get_accessory_values(key) == accessory_values:
                return
            self.add(key, accessory_values)
        except Exception as e:
            raise Exception(str(e))
    
    def get_accessory_data(self, key: str) -> dict:
        x = None
        with self.lock:
            x = self.data[key]
        return x
    
    def get_accessory_values(self, key: str) -> dict:
        x = None
        with self.lock:
            x = self.data[key]['values']
        return x

    def get_accessory_value(self, key: str, characteristicType: str) -> int:
        x = None
        with self.lock:
            if characteristicType in self.data[key]['values']:
                x = self.data[key]['values'][characteristicType]
            else:
                raise Exception("'" + characteristicType + "' is not a characteristic of this accessory.")
        return x

    def get_accessory_serviceName(self, key: str) -> dict:
        x = None
        with self.lock:
            x = self.data[key]['serviceName']
        return x
    
    def get_accessory_date(self, key: str) -> datetime:
        x = None
        with self.lock:
            x = self.data[key]['date']
        return x

    def set_accessory_value(self, key: str, characteristicType: str, value: int) -> None:
        with self.lock:
            if characteristicType in self.data[key]['values']:
                self.data[key]['values'][characteristicType] = value
            else:
                raise Exception("'" + characteristicType + "' is not a characteristic of this accessory.")
            hb.set_accessory_characteristic(key, characteristicType, value)
    
    def restart_homebridge_instance(self) -> None:
        with self.lock:
            hb.restart_homebridge_instance()

# check if database file exists
def check_database_file(path: str = "../db/database") -> bool:
    return os.path.isfile(path)

# save database data to file
def save_database_to_file(db: Database, path: str = "../db/database") -> None:
    dill.dump(db, file = open(path, "wb"))

# load database data from file
def load_database_file(path: str = "../db/database") -> Database:
    db = dill.load(open(path, "rb"))
    return db

# remove database file
def remove_database_file(path: str = "../db/database") -> None:
    os.remove(path)