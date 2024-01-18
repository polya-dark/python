# 1

def get_string_info(s):
    """Функция возвращает кортеж из переданной строки и ее длины."""
    return s, len(s)

# Ввод списка городов
city_names = input("Введите список городов через пробел: ").split()

# Создание словаря из городов и их длин
cities_dict = {city: get_string_info(city) for city in city_names}

# Вывод результата
print("Словарь городов и их длин:")
print(cities_dict)

# 2

# Объявление анонимной функции (лямбда) для вычисления модуля числа
absolute_value = lambda x: abs(x)

# Ввод вещественного числа
input_number = float(input("Введите вещественное число: "))

# Вызов лямбда-функции и вывод результата
result = absolute_value(input_number)
print(f"Модуль числа {input_number} равен:", result)
