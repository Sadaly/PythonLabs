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

# Пользователь выбирает задачу
task_choice = int(input("Выберите функцию (1, 2, 3, 4, or 5):\n1. Дан целочисленный массив, в котором лишь один элемент отличается  от остальных. Необходимо найти значение этого элемента.\n2. Дан целочисленный массив. Необходимо найти два наименьших элемента.\n3. Дано вещественное число R и массив вещественных чисел. Найти элемент массива, который наиболее близок к данному числу.\n4. Для введенного списка положительных чисел построить список всех положительных делителей элементов списка без повторений.\n5. Дан список. Построить новый список из квадратов неотрицательных чисел, меньших 100 и встречающихся в массиве больше 2 раз.\n"))

# В зависимости от выбора пользователя, выполняем соответствующую задачу
if task_choice == 1:
    arr = list(map(int, input("Введите массив чисел (элементы разделены пробелами): ").split()))
    result = FindUniqueElement(arr)
    print(f"Уникальный элемент: {result}")

elif task_choice == 2:
    arr = list(map(int, input("Введите массив чисел (элементы разделены пробелами): ").split()))
    result = FindTwoMinElements(arr)
    print(f"Два наименьших элемента: {result}")

elif task_choice == 3:
    R = float(input("Введите вещественное число R: "))
    arr = list(map(float, input("Введите массив вещественных чисел (элементы разделены пробелами): ").split()))
    result = FindClosestElement(R, arr)
    print(f"Ближайший элемент к {R} это {result}")

elif task_choice == 4:
    nums = list(map(int, input("Введите массив положительных чисел (элементы разделены пробелами): ").split()))
    result = FindPositiveDivisors(nums)
    print(f"Положительные делители: {result}")

elif task_choice == 5:
    arr = list(map(int, input("Введите массив чисел (элементы разделены пробелами): ").split()))
    result = SquaresGreaterThan2(arr)
    print(f"Квадраты элементов повторяющихся больше 2 раз элементов и меньше 100: {result}")


