import time

# Функция для записи строки в файл
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Функция для чтения из файла
def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Засекаем время начала работы программы
start_time = time.time()

# Строка для записи в файл
file_content = "Работа №3. Импорт модулей и пакетов. Работа с файлами"

# Записываем строку в файл out.txt
write_to_file("out.txt", file_content)

# Читаем содержимое файла и выводим на экран
read_content = read_from_file("out.txt")
print("Содержимое файла:", read_content)

# Засекаем время окончания работы программы
end_time = time.time()

# Вычисляем и выводим время работы программы
execution_time = end_time - start_time
print("Время работы программы:", execution_time, "секунд")
