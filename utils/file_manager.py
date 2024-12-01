import json
import os
from datetime import datetime

class FileManager:
    @staticmethod
    def load_json(file_path):
        if not os.path.exists(file_path):
            return []
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def save_json(file_path, data):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def get_current_timestamp():
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
