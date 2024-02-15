# -*- coding: cp1251 -*-
import random

class Task2: 
    
    # ���� ������. ���������� ���������� ��� ������� ������ � ��������� �������.
    def ShuffleString():
        print('������� ������: ')
        stroka = input()
        print('����������� ������: ' + stroka)
        
        ls = list(stroka)
        random.shuffle(ls)
        
        result = ''.join(ls)
        print('������������ ������: ' + result)
    
    # ���� ������, ��������� �� �������� ��������. ���������� ���������, �������� �� ��������� ������� ���� ������ ���������.
    def IsPalindrome():
        print('������� ������: ')
        stroka = input()
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        upper_case_letters = ''
        
        for i in range(0, len(stroka)):
            if (alphabet.find(stroka[i]) != -1):
                upper_case_letters += stroka[i]
                
        length_upp_cs_ltr = len(upper_case_letters)
        for i in range(0, length_upp_cs_ltr // 2 + length_upp_cs_ltr % 2):
            if (upper_case_letters[i] != upper_case_letters[length_upp_cs_ltr - 1 - i]):
                return False
            
        return True
    