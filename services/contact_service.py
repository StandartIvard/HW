from models.contact import Contact
from utils.file_manager import FileManager

class ContactService:
    FILE_PATH = "data/contacts.json"

    @staticmethod
    def menu():
        while True:
            print("\nУправление контактами:")
            print("1. Добавить новый контакт")
            print("2. Поиск контакта")
            print("3. Редактировать контакт")
            print("4. Удалить контакт")
            print("5. Назад")
            choice = input("Выберите действие: ")

            if choice == '1':
                ContactService.add_contact()
            elif choice == '2':
                ContactService.search_contact()
            elif choice == '3':
                ContactService.edit_contact()
            elif choice == '4':
                ContactService.delete_contact()
            elif choice == '5':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    @staticmethod
    def add_contact():
        name = input("Введите имя контакта: ")
        phone = input("Введите телефон: ")
        email = input("Введите email: ")
        contacts = FileManager.load_json(ContactService.FILE_PATH)
        contact_id = len(contacts) + 1
        new_contact = Contact(contact_id, name, phone, email)
        contacts.append(new_contact.to_dict())
        FileManager.save_json(ContactService.FILE_PATH, contacts)
        print("Контакт успешно добавлен!")

    @staticmethod
    def search_contact():
        search_term = input("Введите имя или телефон для поиска: ")
        contacts = FileManager.load_json(ContactService.FILE_PATH)
        results = [c for c in contacts if search_term.lower() in c["name"].lower() or search_term in c["phone"]]
        if results:
            for contact in results:
                print(f"{contact['id']}. {contact['name']} - {contact['phone']} ({contact['email']})")
        else:
            print("Контакты не найдены.")

    @staticmethod
    def edit_contact():
        contact_id = int(input("Введите ID контакта для редактирования: "))
        contacts = FileManager.load_json(ContactService.FILE_PATH)
        contact = next((c for c in contacts if c["id"] == contact_id), None)
        if not contact:
            print("Контакт не найден.")
            return
        contact["name"] = input(f"Введите новое имя (старое: {contact['name']}): ") or contact["name"]
        contact["phone"] = input(f"Введите новый телефон (старый: {contact['phone']}): ") or contact["phone"]
        contact["email"] = input(f"Введите новый email (старый: {contact['email']}): ") or contact["email"]
        FileManager.save_json(ContactService.FILE_PATH, contacts)
        print("Контакт успешно обновлен!")

    @staticmethod
    def delete_contact():
        contact_id = int(input("Введите ID контакта для удаления: "))
        contacts = FileManager.load_json(ContactService.FILE_PATH)
        contacts = [c for c in contacts if c["id"] != contact_id]
        FileManager.save_json(ContactService.FILE_PATH, contacts)
        print("Контакт успешно удален!")
