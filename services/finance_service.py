from models.finance_record import FinanceRecord
from utils.file_manager import FileManager

class FinanceService:
    FILE_PATH = "data/finance.json"

    @staticmethod
    def menu():
        while True:
            print("\nУправление финансовыми записями:")
            print("1. Добавить новую запись")
            print("2. Просмотреть все записи")
            print("3. Удалить запись")
            print("4. Назад")
            choice = input("Выберите действие: ")

            if choice == '1':
                FinanceService.add_record()
            elif choice == '2':
                FinanceService.view_records()
            elif choice == '3':
                FinanceService.delete_record()
            elif choice == '4':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    @staticmethod
    def add_record():
        amount = float(input("Введите сумму операции (положительное число для дохода, отрицательное для расхода): "))
        category = input("Введите категорию операции: ")
        date = input("Введите дату операции (ДД-ММ-ГГГГ): ")
        description = input("Введите описание операции: ")
        records = FileManager.load_json(FinanceService.FILE_PATH)
        record_id = len(records) + 1
        new_record = FinanceRecord(record_id, amount, category, date, description)
        records.append(new_record.to_dict())
        FileManager.save_json(FinanceService.FILE_PATH, records)
        print("Финансовая запись успешно добавлена!")

    @staticmethod
    def view_records():
        records = FileManager.load_json(FinanceService.FILE_PATH)
        if not records:
            print("Нет записей.")
            return
        for record in records:
            print(f"{record['id']}. {record['date']} - {record['amount']} ({record['category']}) - {record['description']}")

    @staticmethod
    def delete_record():
        record_id = int(input("Введите ID записи для удаления: "))
        records = FileManager.load_json(FinanceService.FILE_PATH)
        records = [r for r in records if r["id"] != record_id]
        FileManager.save_json(FinanceService.FILE_PATH, records)
        print("Финансовая запись успешно удалена!")
