# 1
def is_odd(number):
    """Проверяет, является ли число нечетным."""
    return number % 2 != 0

# Ввод списка целых чисел
input_numbers = input("Введите список целых чисел через пробел: ")
numbers_list = list(map(int, input_numbers.split()))

# Формирование списка из нечетных значений
odd_values = [num for num in numbers_list if is_odd(num)]

# Вывод результата
print("Список из нечетных значений:")
print(odd_values)

# 2

def fibonacci_sequence(n, current_sequence=None):
    """Рекурсивно формирует последовательность чисел Фибоначчи."""
    if current_sequence is None:
        current_sequence = [1, 1]

    if n <= len(current_sequence):
        return current_sequence[:n]

    next_value = current_sequence[-1] + current_sequence[-2]
    current_sequence.append(next_value)

    return fibonacci_sequence(n, current_sequence)

# Ввод натурального числа n
n = int(input("Введите натуральное число n: "))

# Формирование и вывод последовательности Фибоначчи
fibonacci_result = fibonacci_sequence(n)
print("Последовательность Фибоначчи:")
print(fibonacci_result)

