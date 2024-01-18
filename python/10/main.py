# 1

def check_string_length(s):
    """Функция, возвращающая False, если длина строки меньше трех символов, иначе True."""
    return len(s) >= 3

# Ввод списка городов
city_names = input("Введите список городов через пробел: ").split()

# Формирование списка из названий городов длиной не менее трех символов
filtered_cities = [city for city in city_names if check_string_length(city)]

# Вывод результата
print("Список городов длиной не менее трех символов:")
print(filtered_cities)

# 2

def flatten_list(input_list):
    """Рекурсивная функция для преобразования многомерного списка в одномерный."""
    result = []
    for item in input_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

# Исходный многомерный список
d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], [True, [1, -1]]], 7.89]

# Вызов функции и вывод результата
flattened_list = flatten_list(d)
print("Одномерный список:")
print(flattened_list)
