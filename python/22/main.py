# 1

def function_closure(f):
    """Функция с замыканием для формирования строки с результатом работы функции."""
    def inner_function(a, b):
        result = f(a, b)
        return f"Для значений {a}, {b} функция f(a, b) = {result}"
    return inner_function

# Пример функции f (можете изменить на свою)
def example_function(a, b):
    return a * b + a + b

# Создание замыкания с переданной функцией
closure_function = function_closure(example_function)

# Ввод значений a и b с клавиатуры
a_input = float(input("Введите значение a: "))
b_input = float(input("Введите значение b: "))

# Вызов внутренней функции через замыкание и вывод результата
result_string = closure_function(a_input, b_input)
print(result_string)

# 2

from math import pi

def area_decorator(func):
    """Декоратор для вывода сообщения о площади круга."""
    def wrapper(radius):
        result = func(radius)
        print(f"Площадь круга равна = {result:.2f}")
        return result
    return wrapper

@area_decorator
def calculate_circle_area(radius):
    """Функция для вычисления площади круга."""
    return pi * radius ** 2

# Ввод радиуса с клавиатуры
radius_input = float(input("Введите радиус круга: "))

# Вызов декорированной функции и вывод результата
result_area = calculate_circle_area(radius_input)
