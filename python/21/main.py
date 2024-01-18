# 1

def area_calculation_closure(type=0):
    """Функция с замыканием для вычисления площади фигуры (треугольника или прямоугольника)."""
    def inner_function(param1, param2):
        """Внутренняя функция для вычисления площади в зависимости от типа фигуры."""
        if type == 0:  # Треугольник
            return 0.5 * param1 * param2
        else:  # Прямоугольник (или любая другая фигура)
            return param1 * param2
    return inner_function

# Ввод параметров и типа фигуры с клавиатуры
type_input = int(input("Введите тип фигуры (0 для треугольника, 1 для прямоугольника): ") or 0)
param1_input = float(input("Введите первый параметр: "))
param2_input = float(input("Введите второй параметр: "))

# Создание замыкания с переданным типом фигуры
area_closure_function = area_calculation_closure(type_input)

# Вызов внутренней функции через замыкание и вывод результата
result_area = area_closure_function(param1_input, param2_input)
print("Результат вычисления площади фигуры:", result_area)

# 2

def perimeter_decorator(func):
    """Декоратор для вывода сообщения о периметре фигуры."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Периметр фигуры равен = {result}")
        return result
    return wrapper

@perimeter_decorator
def calculate_perimeter(sides):
    """Функция для вычисления периметра многоугольника."""
    return sum(sides)

# Ввод длин сторон многоугольника с клавиатуры
sides_input = list(map(float, input("Введите длины сторон многоугольника через пробел: ").split()))

# Вызов декорированной функции и вывод результата
result_perimeter = calculate_perimeter(sides_input)
