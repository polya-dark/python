import time

# Функция для создания таблицы умножения и сохранения в файл
def create_and_save_multiplication_table():
    multiplication_table = []
    for i in range(1, 11):
        row = []
        for j in range(1, 11):
            row.append((i, j, i * j))
        multiplication_table.append(tuple(row))
    
    # Сохранить таблицу умножения в файл
    with open("multiplication_table.txt", "w") as file:
        for row in multiplication_table:
            file.write(" ".join(map(str, row)) + "\n")

# Функция для чтения данных из файла и формирования двумерного кортежа
def read_and_create_tuple():
    read_multiplication_table = []
    with open("multiplication_table.txt", "r") as file:
        for line in file:
            row = tuple(map(int, line.strip().split()))
            read_multiplication_table.append(row)
    
    return tuple(read_multiplication_table)

# Измерить время выполнения
start_time = time.time()

# Создать и сохранить таблицу умножения
create_and_save_multiplication_table()

# Прочитать и создать двумерный кортеж
result_tuple = read_and_create_tuple()

# Вывести на экран кортеж и время работы программы
print("Двумерный кортеж таблицы умножения:")
print(result_tuple)
print("Время выполнения программы: %.5f секунд" % (time.time() - start_time))
