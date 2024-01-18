# 1

import re

def is_valid_email(email):
    """Функция для проверки корректности email-адреса."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Ввод email-адреса
email_input = input("Введите email-адрес: ")

# Вызов функции и вывод результата
result = is_valid_email(email_input)
if result:
    print("Введенный email-адрес корректен.")
else:
    print("Введенный email-адрес некорректен.")

# 2
    
# Объявление анонимной функции (лямбда) для определения вхождения фрагмента "ra"
contains_ra_fragment = lambda x: 'ra' in x

# Ввод строки
input_string = input("Введите строку: ")

# Вызов лямбда-функции и вывод результата
result = contains_ra_fragment(input_string)
print("Фрагмент 'ra' присутствует в строке:", result)
