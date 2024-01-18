import math

# Вычисление логарифма по основанию 2 для целых чисел от 1 до 10
log_values = [math.log2(x) for x in range(1, 11)]

# Сохранение списка в файл в бинарном режиме
with open("log_values.bin", "wb") as file:
    file.write(bytes(log_values))

# Чтение из файла в другой список
read_log_values = list(bytearray(open("log_values.bin", "rb").read()))

# Вывод на экран прочитанных данных
print("Прочитанный список:", read_log_values)
