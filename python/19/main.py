# 1

def template_closure(template):
    """Функция с замыканием, подставляющая фамилию и имя в шаблон."""
    def inner_function(last_name, first_name):
        """Внутренняя функция, подставляющая данные в шаблон и возвращающая результат."""
        result = template.replace("%F%", last_name).replace("%N%", first_name)
        return result
    return inner_function

# Ввод шаблона, фамилии и имени с клавиатуры
template_input = input("Введите шаблон: ")
last_name_input = input("Введите фамилию: ")
first_name_input = input("Введите имя: ")

# Создание замыкания с переданным шаблоном
template_closure_function = template_closure(template_input)

# Вызов внутренней функции через замыкание и вывод результата
result_message = template_closure_function(last_name_input, first_name_input)
print("Результат замыкания:", result_message)


# 2

def sum_decorator(func):
    """Декоратор для вычисления суммы чисел с заданным начальным значением."""
    def wrapper(*args, **kwargs):
        start_value = kwargs.get('start', 0)
        result = func(*args, **kwargs)
        return start_value + result
    return wrapper

@sum_decorator
def sum_of_numbers(input_string):
    """Функция для преобразования строки в список чисел и вычисления их суммы."""
    numbers = list(map(int, input_string.split()))
    return sum(numbers)

# Ввод строки с числами через пробел
numbers_input = input("Введите строку с числами через пробел: ")

# Вызов декорированной функции sum_of_numbers и вывод результата
start_value_input = int(input("Введите начальное значение для суммы (по умолчанию 0): ") or 0)
result_sum = sum_of_numbers(numbers_input, start=start_value_input)
print(f"Сумма чисел с начальным значением {start_value_input}: {result_sum}")
