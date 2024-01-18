# 1

def collection_converter(type):
    """Функция с замыканием, преобразующая строку из списка чисел в список или кортеж."""
    def inner_function(numbers_string):
        """Внутренняя функция, выполняющая преобразование в список или кортеж."""
        numbers = list(map(int, numbers_string.split()))
        if type == 'list':
            return numbers
        elif type == 'tuple':
            return tuple(numbers)
        else:
            raise ValueError("Некорректный тип. Допустимые значения: 'list' или 'tuple'")
    return inner_function

# Ввод типа коллекции и строки с числами через пробел
type_input = input("Введите тип коллекции ('list' или 'tuple'): ")
numbers_input = input("Введите список чисел через пробел: ")

# Создание замыкания с переданным типом коллекции
converter_closure_function = collection_converter(type_input)

# Вызов внутренней функции через замыкание и вывод результата
result_collection = converter_closure_function(numbers_input)
print("Результат преобразования:", result_collection)


# 2

def dict_from_lists_decorator(func):
    """Декоратор для преобразования двух списков в словарь."""
    def wrapper(*args, **kwargs):
        list1, list2 = func(*args, **kwargs)
        result_dict = dict(zip(list1, list2))
        return result_dict
    return wrapper

@dict_from_lists_decorator
def get_lists_from_input():
    """Функция для ввода двух строк и преобразования их в два списка."""
    words1 = input("Введите первый список слов через пробел: ").split()
    words2 = input("Введите второй список слов через пробел: ").split()
    return words1, words2

# Вызов декорированной функции и вывод результата
result_dict = get_lists_from_input()
print("Словарь из двух списков:", result_dict)
