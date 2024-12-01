import json
from models.task import Task
from utils.file_manager import FileManager

class TaskService:
    FILE_PATH = "data/tasks.json"

    @staticmethod
    def menu():
        while True:
            print("\nУправление задачами:")
            print("1. Добавить новую задачу")
            print("2. Просмотреть задачи")
            print("3. Отметить задачу как выполненную")
            print("4. Редактировать задачу")
            print("5. Удалить задачу")
            print("6. Назад")
            choice = input("Выберите действие: ")

            if choice == '1':
                TaskService.create_task()
            elif choice == '2':
                TaskService.view_tasks()
            elif choice == '3':
                TaskService.mark_task_done()
            elif choice == '4':
                TaskService.edit_task()
            elif choice == '5':
                TaskService.delete_task()
            elif choice == '6':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    @staticmethod
    def create_task():
        title = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")
        priority = input("Введите приоритет (Высокий/Средний/Низкий): ")
        due_date = input("Введите срок выполнения (ДД-ММ-ГГГГ): ")
        tasks = FileManager.load_json(TaskService.FILE_PATH)
        task_id = len(tasks) + 1
        new_task = Task(task_id, title, description, False, priority, due_date)
        tasks.append(new_task.to_dict())
        FileManager.save_json(TaskService.FILE_PATH, tasks)
        print("Задача успешно добавлена!")

    @staticmethod
    def view_tasks():
        tasks = FileManager.load_json(TaskService.FILE_PATH)
        if not tasks:
            print("Нет задач.")
            return
        for task in tasks:
            status = "Выполнено" if task["done"] else "Не выполнено"
            print(f"{task['id']}. {task['title']} [{task['priority']}] - {status} (Срок: {task['due_date']})")

    @staticmethod
    def mark_task_done():
        task_id = int(input("Введите ID задачи для отметки как выполненной: "))
        tasks = FileManager.load_json(TaskService.FILE_PATH)
        task = next((t for t in tasks if t["id"] == task_id), None)
        if task:
            task["done"] = True
            FileManager.save_json(TaskService.FILE_PATH, tasks)
            print("Задача отмечена как выполненная.")
        else:
            print("Задача не найдена.")

    @staticmethod
    def edit_task():
        task_id = int(input("Введите ID задачи для редактирования: "))
        tasks = FileManager.load_json(TaskService.FILE_PATH)
        task = next((t for t in tasks if t["id"] == task_id), None)
        if not task:
            print("Задача не найдена.")
            return
        task["title"] = input(f"Введите новое название (старое: {task['title']}): ") or task["title"]
        task["description"] = input(f"Введите новое описание (старое: {task['description']}): ") or task["description"]
        task["priority"] = input(f"Введите новый приоритет (старый: {task['priority']}): ") or task["priority"]
        task["due_date"] = input(f"Введите новый срок (старый: {task['due_date']}): ") or task["due_date"]
        FileManager.save_json(TaskService.FILE_PATH, tasks)
        print("Задача успешно обновлена!")

    @staticmethod
    def delete_task():
        task_id = int(input("Введите ID задачи для удаления: "))
        tasks = FileManager.load_json(TaskService.FILE_PATH)
        tasks = [t for t in tasks if t["id"] != task_id]
        FileManager.save_json(TaskService.FILE_PATH, tasks)
        print("Задача успешно удалена!")
