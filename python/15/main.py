# 16

# 1

def get_name_info():
    """Функция для считывания фамилии, имени и отчества с клавиатуры и возвращения в виде кортежа."""
    full_name = input("Введите фамилию, имя и отчество через пробел: ")
    last_name, first_name, middle_name = full_name.split()
    return last_name, first_name, middle_name

# Вызов функции и вывод результата
last_name, first_name, middle_name = get_name_info()
print(f"Уважаемый, {first_name} {last_name}! Вы верно выполнили данную работу!")

# 2

def filter_tuple_values(tuple_values, filter_func):
    """Рекурсивная функция для фильтрации значений кортежа с использованием переданной функции."""
    if not tuple_values:
        return []
    current_element = tuple_values[0]
    if isinstance(current_element, tuple):
        filtered_values = filter_tuple_values(current_element, filter_func)
    else:
        filtered_values = [current_element] if filter_func(current_element) else []
    return filtered_values + filter_tuple_values(tuple_values[1:], filter_func)

# Ввод кортежа значений
input_tuple = input("Введите кортеж значений через запятую (без пробелов): ")
values_tuple = eval(input_tuple)  # Внимание: использование eval, так как вопрос описывает ввод без пробелов

# Объявление анонимной функции (лямбда) для фильтрации значений
filter_function = lambda x: isinstance(x, int) and x % 2 == 0  # Пример: фильтр четных чисел

# Вызов функции и вывод результата
filtered_result = filter_tuple_values(values_tuple, filter_function)
print("Отфильтрованный список значений кортежа:")
print(filtered_result)
