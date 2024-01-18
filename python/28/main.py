import math
import json

# Вычисление факториала и формирование словаря
factorial_dict = {n: math.factorial(n) for n in range(1, 11)}

# Сохранение словаря в файл в текстовом режиме
with open("factorial_data.txt", "w") as file:
    json.dump(factorial_dict, file)

# Чтение из файла в другой словарь
read_factorial_dict = {}
with open("factorial_data.txt", "r") as file:
    read_factorial_dict = json.load(file)

# Вывод на экран прочитанных данных (словарь)
print("Прочитанный словарь:", read_factorial_dict)
