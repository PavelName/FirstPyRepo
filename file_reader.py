print('Hi Gys!!!')

def calculator():
    print("--- Простой калькулятор ---")
    print("Введите 'exit', чтобы выйти")

    while True:
        # Получаем данные от пользователя
        user_input = input("\nВведите пример (например, 2 + 2) или 'exit': ")

        if user_input.lower() == 'exit':
            print("До свидания!")
            break

        try:
            # Разделяем строку на части: число1, операция, число2
            parts = user_input.split()
            
            # Проверка, что введены все 3 части
            if len(parts) != 4:
                print("Ошибка! Вводите через пробел: Число Операция Число")
                continue

            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            # Выполняем расчет
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = num1 / num2
            else:
                print("Неверный оператор! Доступны: +, -, *, /")
                continue

            print(f"Результат: {result}")

        except ValueError:
            print("Ошибка! Вводите только числа.")

# Запуск программы
calculator()
