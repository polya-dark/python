import numpy as np

# Чтение матрицы из файла
file_path = "matrix.txt"

matrix = np.loadtxt(file_path)

# Вычисление определителя
determinant = np.linalg.det(matrix)

# Запись результата в файл
result_file_path = "result.txt"
with open(result_file_path, "w") as result_file:
    result_file.write(f"Определитель матрицы:\n{determinant}")

print(f"Определитель матрицы успешно вычислен и записан в файл '{result_file_path}'.")