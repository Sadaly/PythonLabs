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
    
    # Функция 2 Найти минимальную нечетную цифру числа.
    def MinOddNumber(number):
        num_str = str(number)
        minimal_number = 11
        
        for symbol in num_str:
            current_num = int(symbol)
            if (current_num % 2 == 1 and current_num < minimal_number):
                minimal_number = current_num
            if (current_num == 1):
                break
                
        if (minimal_number == 11):
            print('В этом числе нет такой цифры')
        else:
            print(minimal_number)
    
