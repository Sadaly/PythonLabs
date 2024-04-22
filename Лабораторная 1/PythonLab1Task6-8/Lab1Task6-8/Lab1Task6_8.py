# -*- coding: cp1251 -*-
import re

def MaxLettersInARow(stroka):
    alphabet = '�����Ũ����������������������������������������������������������'
    counter = 0
    max_counter = 0

    for i in range(0, len(alphabet)):
        if(alphabet.find(stroka[i]) != -1):
            for j in range(0, len(stroka)-1):
                if(alphabet.find(stroka[j]) != -1 and alphabet.find(stroka[j + 1]) != -1):
                    counter += 1
                elif (counter != 0):
                    if(counter > max_counter):
                        max_counter = counter
                    counter = 0
            return max_counter + 1
    return 0
    
def MinNaturalNumber(stroka):
    numbers = [int(i) for i in re.findall(r'\d+', stroka)]
    min_number = min(numbers)
    return min_number

def FindMaxConsecutiveDigits(stroka):
    found_digits = re.findall(r'\d+', stroka)
    max_length = max(len(digits) for digits in found_digits)
    return max_length

# ������������ �������� ������
task_choice = int(input("�������� ������� (1, 2, 3): \n1.���� ������. ���������� ����� ���������� ���������� ������ ������ �������� ���������.\n2.���� ������. ���������� ����� ����������� �� ��������� � ��� ����������� �����.\n3.���� ������. ���������� ����� ���������� ���������� ������ ������ ����.\n"))

# � ����������� �� ������ ������������, ��������� ��������������� ������
if task_choice == 1:
    print()
    arr = input()
    result = MaxLettersInARow(arr)
    print(f"{result}")

elif task_choice == 2:
    print()
    arr = input()
    result = MinNaturalNumber(arr)
    print(f"{result}")

elif task_choice == 3:
    print()
    arr = input()
    result = FindMaxConsecutiveDigits(arr)
    print(f"{result}")
