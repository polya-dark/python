# 1

def get_sq(max_value, min_value):
    """Функция для вычисления произведения максимального и минимального значений."""
    return max_value * min_value

# Ввод списка целых чисел
input_numbers = input("Введите список целых чисел через пробел: ")
numbers_list = list(map(int, input_numbers.split()))

# Вызов функции get_sq с максимальным и минимальным значениями из списка
result = get_sq(max(numbers_list), min(numbers_list))
print("Произведение максимального и минимального значений списка:", result)

# 2

def filter_list(input_list, filter_func):
    """Функция для фильтрации списка с использованием переданной функции."""
    return [item for item in input_list if filter_func(item)]

# Ввод списка целых чисел
input_numbers = input("Введите список целых чисел через пробел: ")
numbers_list = list(map(int, input_numbers.split()))

# Объявление лямбда-функции для отбора элементов
filter_function = lambda x: x % 2 == 0  # Пример: фильтр четных чисел

# Вызов функции filter_list и вывод результата
filtered_result = filter_list(numbers_list, filter_function)
print("Отфильтрованный список:", filtered_result)
