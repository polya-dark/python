import random
import struct

# Генерация 100 случайных чисел
random_numbers = [random.random() for _ in range(100)]

# Сохранение списка в файл в бинарном режиме
with open("random_numbers.bin", "wb") as file:
    file.write(struct.pack('100d', *random_numbers))

# Чтение из файла в другой список
read_random_numbers = []
with open("random_numbers.bin", "rb") as file:
    packed_data = file.read()
    read_random_numbers = struct.unpack('100d', packed_data)

# Вывод на экран прочитанных данных
print("Прочитанный список:", read_random_numbers)
