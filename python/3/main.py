import numpy as np

# Чтение матрицы из файла
file_path = "matrix.txt"
try:
    matrix = np.loadtxt(file_path)
except FileNotFoundError:
    print(f"Файл '{file_path}' не найден.")
    exit()

# Транспонирование матрицы
transposed_matrix = np.transpose(matrix)

# Запись результата в файл
result_file_path = "transposed_matrix.txt"
np.savetxt(result_file_path, transposed_matrix)

print(f"Транспонированная матрица успешно записана в файл '{result_file_path}'.")
