from services.note_service import NoteService
from services.task_service import TaskService
from services.contact_service import ContactService
from services.finance_service import FinanceService
from services.calculator import Calculator

def main():
    while True:
        print("\nДобро пожаловать в Персональный помощник!")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансовыми записями")
        print("5. Калькулятор")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            NoteService.menu()
        elif choice == '2':
            TaskService.menu()
        elif choice == '3':
            ContactService.menu()
        elif choice == '4':
            FinanceService.menu()
        elif choice == '5':
            Calculator.run()
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
