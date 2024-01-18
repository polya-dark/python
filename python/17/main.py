# 1

def tag_closure(tag):
    """Функция с замыканием, заключающая переданную строку в тег."""
    def inner_function(content):
        """Внутренняя функция, добавляющая тег к строке."""
        return f"<{tag}>{content}</{tag}>"
    return inner_function

# Ввод тега и содержимого с клавиатуры
tag_input = input("Введите тег: ")
content_input = input("Введите содержимое: ")

# Создание замыкания с переданным тегом
tag_closure_function = tag_closure(tag_input)

# Вызов внутренней функции через замыкание
result = tag_closure_function(content_input)
print("Результат:", result)

# 2

def sort_decorator(func):
    """Декоратор для сортировки списка чисел."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        sorted_result = sorted(result)
        return sorted_result
    return wrapper

@sort_decorator
def get_list(input_string):
    """Функция для преобразования строки в список чисел."""
    numbers = list(map(int, input_string.split()))
    return numbers

# Ввод строки с числами через пробел
numbers_input = input("Введите строку с числами через пробел: ")

# Вызов декорированной функции get_list и вывод результата
sorted_numbers = get_list(numbers_input)
print("Отсортированный список чисел:", sorted_numbers)
