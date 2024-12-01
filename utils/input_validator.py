import re

class InputValidator:
    @staticmethod
    def validate_date(date):
        pattern = r"\d{2}-\d{2}-\d{4}"
        if not re.match(pattern, date):
            raise ValueError("Неверный формат даты. Используйте формат ДД-ММ-ГГГГ.")
        return date

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            raise ValueError("Неверный формат email.")
        return email

    @staticmethod
    def validate_phone(phone):
        pattern = r"^\+?\d{10,15}$"
        if not re.match(pattern, phone):
            raise ValueError("Неверный формат телефона.")
        return phone
