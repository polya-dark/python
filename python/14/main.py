# 1

def calculate_statistics(numbers):
    """Функция для нахождения максимального, минимального и суммы значений в списке."""
    max_value = max(numbers)
    min_value = min(numbers)
    sum_values = sum(numbers)
    return max_value, min_value, sum_values

# Ввод списка чисел
input_numbers = input("Введите список чисел через пробел: ")
numbers_list = list(map(int, input_numbers.split()))

# Вызов функции и вывод результата
result_tuple = calculate_statistics(numbers_list)
print("Максимальное, минимальное и сумма значений в списке:")
print(result_tuple)

# 2

def find_min_value_recursive(tuple_values, current_min=float('inf')):
    """Рекурсивная функция для нахождения минимального значения в кортеже."""
    if not tuple_values:
        return current_min
    current_element = tuple_values[0]
    if isinstance(current_element, tuple):
        current_min = find_min_value_recursive(current_element, current_min)
    elif current_element < current_min:
        current_min = current_element
    return find_min_value_recursive(tuple_values[1:], current_min)

# Ввод кортежа чисел
input_tuple = input("Введите кортеж чисел через запятую (без пробелов): ")
values_tuple = eval(input_tuple)  # Внимание: использование eval, так как вопрос описывает ввод без пробелов

# Вызов функции и вывод результата
min_value = find_min_value_recursive(values_tuple)
print("Минимальное значение в кортеже:", min_value)
