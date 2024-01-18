
def isEven(number):
	return number % 2 == 0

while True:
	user_input = int(input("Enter number: "))

	if user_input == 1:
		break

	if isEven(user_input) == True:
		print(f"Число {user_input} четное!")
	else:
		print(f"Число {user_input} нечетное!")

		
def recursive_sum(lst, index=0):
    """Рекурсивно вычисляет сумму элементов списка."""
    if index == len(lst):
        return 0
    return lst[index] + recursive_sum(lst, index + 1)

# Ввод списка целых чисел
input_numbers = input("Введите список целых чисел через пробел: ")
numbers_list = list(map(int, input_numbers.split()))

# Вычисление и вывод суммы
result_sum = recursive_sum(numbers_list)
print(f"Сумма введенных чисел: {result_sum}")
