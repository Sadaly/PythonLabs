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
    
    # Функция 3 Найти сумму всех делителей числа, взаимно простых с суммой цифр числа и не взаимно простых с произведением цифр числа.
    def Sums(number):
        # Проверяет является ли 2 числа взаимно простыми
        def IsMutPrime(a, b):
            if (a > b):
                temp = a
                a = b
                b = temp
                
            if (a == b):
                print('\t\t' + str(a) + ' не взаимно простое число с ' + str(b))
                return False
            
            for i in range(2, a + 1):
                if (a % i == 0 and b % i == 0):
                    print('\t\t' + str(a) + ' не взаимно простое число с ' + str(b))
                    return False
                
            print('\t\t' + str(a) + ' взаимно простое число с ' + str(b))
            return True
        
        # Сложить все цифры числа
        def NumbersSum(number_str):
            summ = 0
            for symbol in number_str:
                summ += int(symbol)
            
            return summ
        
        # Умножить все цифры числа
        def NumbersMult(number_str):
            mult = 1
            for symbol in number_str:
                mult *= int(symbol)
            
            return mult

        num_str = str(number)
        numbers_sum = NumbersSum(num_str)
        numbers_mult = NumbersMult(num_str)
        
        sum_mut_prime = 0
        sum_mut_not_prime = 0
                    
        print('Сумма цифр числа: ' + str(numbers_sum) + '\nПроизведение цифр числа: ' + str(numbers_mult) + '\n')
        
        def Foo(i):
            print('\tЧисло ' + str(i) + ' делитель числа ' + str(number))
            if(IsMutPrime(i, numbers_sum)):
                sum_mut_prime += i
            if not(IsMutPrime(i, numbers_mult)):
                sum_mut_not_prime += i

        for i in range(2, int(math.sqrt(number))+ 1):
            Foo(i)
                    
        print('\tЧисло ' + str(number) + ' делитель числа ' + str(number))
        if(IsMutPrime(number, numbers_sum)):
            sum_mut_prime += number
        if not(IsMutPrime(number, numbers_mult)):
            sum_mut_not_prime += number
                    
        print('\nСумма всех делителей числа (' + str(number)+ ') взаимно простых с суммой цифр числа равна: '
              + str(sum_mut_prime) + '\n' +
              'Сумма всех делителей числа (' + str(number)+ ') не взаимно простых с произведением цифр числа равна:'
              + str(sum_mut_not_prime) + '\n')
            