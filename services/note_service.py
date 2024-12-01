import json
from models.note import Note
from utils.file_manager import FileManager

class NoteService:
    FILE_PATH = "data/notes.json"

    @staticmethod
    def menu():
        while True:
            print("\nУправление заметками:")
            print("1. Создать заметку")
            print("2. Просмотреть все заметки")
            print("3. Просмотреть заметку")
            print("4. Редактировать заметку")
            print("5. Удалить заметку")
            print("6. Назад")
            choice = input("Выберите действие: ")

            if choice == '1':
                NoteService.create_note()
            elif choice == '2':
                NoteService.view_notes()
            elif choice == '3':
                NoteService.view_note_details()
            elif choice == '4':
                NoteService.edit_note()
            elif choice == '5':
                NoteService.delete_note()
            elif choice == '6':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    @staticmethod
    def create_note():
        title = input("Введите заголовок заметки: ")
        content = input("Введите содержание заметки: ")
        timestamp = FileManager.get_current_timestamp()
        notes = FileManager.load_json(NoteService.FILE_PATH)
        note_id = len(notes) + 1
        new_note = Note(note_id, title, content, timestamp)
        notes.append(new_note.to_dict())
        FileManager.save_json(NoteService.FILE_PATH, notes)
        print("Заметка успешно создана!")

    @staticmethod
    def view_notes():
        notes = FileManager.load_json(NoteService.FILE_PATH)
        if not notes:
            print("Нет заметок.")
            return
        for note in notes:
            print(f"{note['id']}. {note['title']} ({note['timestamp']})")

    @staticmethod
    def view_note_details():
        note_id = int(input("Введите ID заметки: "))
        notes = FileManager.load_json(NoteService.FILE_PATH)
        note = next((n for n in notes if n["id"] == note_id), None)
        if note:
            print(f"Заголовок: {note['title']}")
            print(f"Содержание: {note['content']}")
            print(f"Дата: {note['timestamp']}")
        else:
            print("Заметка не найдена.")

    @staticmethod
    def edit_note():
        note_id = int(input("Введите ID заметки для редактирования: "))
        notes = FileManager.load_json(NoteService.FILE_PATH)
        note = next((n for n in notes if n["id"] == note_id), None)
        if not note:
            print("Заметка не найдена.")
            return
        note["title"] = input(f"Введите новый заголовок (старый: {note['title']}): ") or note["title"]
        note["content"] = input(f"Введите новое содержание (старое: {note['content']}): ") or note["content"]
        note["timestamp"] = FileManager.get_current_timestamp()
        FileManager.save_json(NoteService.FILE_PATH, notes)
        print("Заметка успешно обновлена!")

    @staticmethod
    def delete_note():
        note_id = int(input("Введите ID заметки для удаления: "))
        notes = FileManager.load_json(NoteService.FILE_PATH)
        notes = [n for n in notes if n["id"] != note_id]
        FileManager.save_json(NoteService.FILE_PATH, notes)
        print("Заметка успешно удалена!")
