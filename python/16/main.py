# 1

def outer_function():
    """Внешняя функция, возвращающая вложенную функцию."""
    def inner_function(x):
        """Вложенная функция, увеличивающая значение x на 5."""
        return x + 5
    return inner_function

# Получение ссылки на внутреннюю функцию
cnt = outer_function()

# Ввод значения k с клавиатуры
k = int(input("Введите значение k: "))

# Вызов внутренней функции через переменную cnt
result = cnt(k)
print("Результат увеличения на 5:", result)

# 2

def func_show(func):
    """Декоратор для отображения результата на экране."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Площадь прямоугольника: {result}")
        return result
    return wrapper

@func_show
def get_sq(width, height):
    """Функция для вычисления площади прямоугольника."""
    return width * height

# Ввод ширины и высоты прямоугольника с клавиатуры
width = float(input("Введите ширину прямоугольника: "))
height = float(input("Введите высоту прямоугольника: "))

# Вызов декорированной функции get_sq
get_sq(width, height)
