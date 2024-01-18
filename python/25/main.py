import random

# Генерация списка из 100 случайных чисел в диапазоне [-2, 5]
random_numbers = [random.randint(-2, 5) for _ in range(100)]

# Сохранение списка в файл в текстовом режиме
with open("random_numbers.txt", "w") as file:
    for number in random_numbers:
        file.write(str(number) + '\n')

# Чтение из файла в другой список
read_random_numbers = []
with open("random_numbers.txt", "r") as file:
    for line in file:
        read_random_numbers.append(int(line.strip()))

# Вывод на экран прочитанных данных
print("Прочитанный список:", read_random_numbers)
