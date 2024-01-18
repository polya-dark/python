import math

# Вычисление логарифма по основанию 10 для целых чисел от 1 до 10
log_values = {round(math.log10(x), 3) for x in range(1, 11)}

# Сохранение множества в файл в текстовом режиме
with open("log_values.txt", "w") as file:
    file.write(" ".join(map(str, log_values)))

# Чтение из файла в другое множество
read_log_values = set()
with open("log_values.txt", "r") as file:
    read_log_values.update(map(float, file.read().split()))

# Вывод на экран прочитанных данных
print("Прочитанное множество:", read_log_values)
