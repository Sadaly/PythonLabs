# -*- coding:cp1251 -*-
from collections import Counter

def FindUniqueElement(arr):
    counter = Counter(arr)
    for num, count in counter.items():
        if count == 1:
            return num
    return None

def FindTwoMinElements(arr):
    if len(arr) < 2:
        return None
    sorted_arr = sorted(arr)
    return sorted_arr[:2]

def FindClosestElement(R, arr):
    if not arr:
        return None
    closest_element = min(arr, key=lambda x: abs(x - R))
    return closest_element

def FindPositiveDivisors(nums):
    unique_divisors = set()

    for num in nums:
        for i in range(1, num + 1):
            if num % i == 0:
                unique_divisors.add(i)

    return list(unique_divisors)

def SquaresGreaterThan2(arr):
    unique_squares = set()
    result = []

    for num in arr:
        square = num**2
        if num >= 0 and square < 100 and arr.count(num) > 2 and square not in unique_squares:
            result.append(square)
            unique_squares.add(square)

    return result

# ������������ �������� ������
task_choice = int(input("�������� ������� (1, 2, 3, 4, or 5):\n1. ��� ������������� ������, � ������� ���� ���� ������� ����������  �� ���������. ���������� ����� �������� ����� ��������.\n2. ��� ������������� ������. ���������� ����� ��� ���������� ��������.\n3. ���� ������������ ����� R � ������ ������������ �����. ����� ������� �������, ������� �������� ������ � ������� �����.\n4. ��� ���������� ������ ������������� ����� ��������� ������ ���� ������������� ��������� ��������� ������ ��� ����������.\n5. ��� ������. ��������� ����� ������ �� ��������� ��������������� �����, ������� 100 � ������������� � ������� ������ 2 ���.\n"))

# � ����������� �� ������ ������������, ��������� ��������������� ������
if task_choice == 1:
    arr = list(map(int, input("������� ������ ����� (�������� ��������� ���������): ").split()))
    result = FindUniqueElement(arr)
    print(f"���������� �������: {result}")

elif task_choice == 2:
    arr = list(map(int, input("������� ������ ����� (�������� ��������� ���������): ").split()))
    result = FindTwoMinElements(arr)
    print(f"��� ���������� ��������: {result}")

elif task_choice == 3:
    R = float(input("������� ������������ ����� R: "))
    arr = list(map(float, input("������� ������ ������������ ����� (�������� ��������� ���������): ").split()))
    result = FindClosestElement(R, arr)
    print(f"��������� ������� � {R} ��� {result}")

elif task_choice == 4:
    nums = list(map(int, input("������� ������ ������������� ����� (�������� ��������� ���������): ").split()))
    result = FindPositiveDivisors(nums)
    print(f"������������� ��������: {result}")

elif task_choice == 5:
    arr = list(map(int, input("������� ������ ����� (�������� ��������� ���������): ").split()))
    result = SquaresGreaterThan2(arr)
    print(f"�������� ��������� ������������� ������ 2 ��� ��������� � ������ 100: {result}")


