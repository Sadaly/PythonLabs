# -*- coding:cp1251 -*-

strings = []
num_strings = int(input("Введите количество строк: "))

for i in range(num_strings):
    string_input = input(f"Введите строку {i+1}: ")
    strings.append(string_input)

sorted_strings = sorted(strings, key=lambda x: len(x.split()))

print("Строки отсортированные по количеству слов:")
for string in sorted_strings:
    print(string)


