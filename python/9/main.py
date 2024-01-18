# 1

def get_sq(length, width):
    """Функция для вычисления площади или периметра прямоугольника."""
    if length == "RECT":
        # Если слово RECT, вычисляем и возвращаем площадь
        return int(width) * int(width)
    else:
        # Если другое слово, вычисляем и возвращаем периметр
        return 2 * (int(length) + int(width))

# Ввод слова и размеров прямоугольника
word = input("Введите слово (RECT или другое): ")
length_value = input("Введите длину: ")
width_value = input("Введите ширину: ")

# Вызов функции и вывод результата
result = get_sq(length_value, width_value)
print("Результат:", result)

# 2

def factorial(n):
    """Рекурсивная функция для вычисления факториала числа n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ввод натурального числа n
n = int(input("Введите натуральное число n: "))

# Вызов функции и вывод результата
result = factorial(n)
print(f"Факториал числа {n} равен:", result)
