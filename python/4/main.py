file_path = 'text.txt'

with open(file_path, 'r', encoding='utf-8') as file:
	text = file.read()

words = text.split()
sorted_words = sorted(words)
result_path = "result.txt"

with open(result_path, 'w', encoding='utf-8') as result_file:
	result_file.write("\n".join(sorted_words))