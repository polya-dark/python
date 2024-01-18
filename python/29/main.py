import random
import pickle

# Сформировать двумерный список 5x5 со случайными значениями
matrix = [[random.randint(-5, 5) for _ in range(5)] for _ in range(5)]

# Сохранить двумерный список в файл в бинарном режиме
with open("matrix_data.dat", "wb") as file:
    pickle.dump(matrix, file)

# Прочитать из файла данные в другой двумерный список
read_matrix = []
with open("matrix_data.dat", "rb") as file:
    read_matrix = pickle.load(file)

# Вывести на экран прочитанный двумерный список
print("Прочитанный двумерный список:")
for row in read_matrix:
    print(row)
