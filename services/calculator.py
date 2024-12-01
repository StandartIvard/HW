class Calculator:
    @staticmethod
    def run():
        print("\nКалькулятор:")
        while True:
            expression = input("Введите выражение (или 'назад' для выхода): ")
            if expression.lower() == 'назад':
                break
            try:
                result = eval(expression, {"__builtins__": None}, {})
                print(f"Результат: {result}")
            except ZeroDivisionError:
                print("Ошибка: деление на ноль!")
            except Exception as e:
                print(f"Ошибка: некорректное выражение. {e}")
