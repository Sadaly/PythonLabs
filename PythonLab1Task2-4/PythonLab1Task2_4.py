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


    