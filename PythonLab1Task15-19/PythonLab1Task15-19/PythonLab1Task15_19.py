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
