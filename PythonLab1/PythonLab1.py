# -*- coding: cp1251 -*-
import math

class Task1:
    # Функция 1 Найти количество делителей числа, не делящихся на 3
    def DividersNot3(number):
        counter = 2
        for i in range(2, number//2 + 1):
            if (i % 3 != 0 and number % i == 0):
                counter += 1
                
        print(counter)
    