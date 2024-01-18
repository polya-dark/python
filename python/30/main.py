import math
import pickle

# Вычислить синус для значений от -π до π с шагом 0.1
sin_values = [math.sin(x) for x in range(int(-math.pi * 10), int(math.pi * 10) + 1, 1)]

# Сохранить список в файл в бинарном режиме
with open("sin_values.dat", "wb") as file:
    pickle.dump(sin_values, file)

# Прочитать из файла данные в другой список
read_sin_values = []
with open("sin_values.dat", "rb") as file:
    read_sin_values = pickle.load(file)

# Вывести на экран прочитанный список
print("Прочитанный список значений синуса:")
print(read_sin_values)
