# -*- coding:cp1251 -*-

strings = []
num_strings = int(input("������� ���������� �����: "))

for i in range(num_strings):
    string_input = input(f"������� ������ {i+1}: ")
    strings.append(string_input)

sorted_strings = sorted(strings, key=len)

print("������ ��������������� �� �����:")
for string in sorted_strings:
    print(string)

