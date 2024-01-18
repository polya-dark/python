# 1

def replace_repeated_chars_closure(replace_with):
    """Функция с замыканием, заменяющая повторяющиеся символы в строке."""
    def inner_function(input_string):
        """Внутренняя функция, выполняющая замену повторяющихся символов."""
        unique_chars = set()
        result = ''
        for char in input_string:
            if char not in unique_chars:
                result += char
                unique_chars.add(char)
            else:
                result += replace_with
        return result
    return inner_function

# Ввод символа для замены повторяющихся символов
replace_char = input("Введите символ для замены повторяющихся: ")

# Создание замыкания с переданным символом для замены
replace_closure_function = replace_repeated_chars_closure(replace_char)

# Вызов внутренней функции через замыкание и вывод результата
input_string = input("Введите строку для преобразования: ")
result_replaced = replace_closure_function(input_string)
print("Результат замены повторяющихся символов:", result_replaced)

# 2

def tag_decorator(tag="h1"):
    """Декоратор для заключения строки в тег с указанным именем."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator

@tag_decorator(tag="div")
def lowercase_string(input_string):
    """Функция для преобразования строки в нижний регистр."""
    return input_string.lower()

# Ввод строки для преобразования в нижний регистр
input_string = input("Введите строку для преобразования в нижний регистр: ")

# Вызов декорированной функции и вывод результата
result_tagged = lowercase_string(input_string)
print("Результат с добавлением тега:", result_tagged)
