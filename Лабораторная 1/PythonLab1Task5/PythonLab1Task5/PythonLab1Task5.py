# -*- coding: cp1251 -*-
import re

# ���� ������. ���������� ����� ��� ����, ������� ������� � ���� "31 ������� 2007".
class Task5:
    text = "afs 31 ������� 2007 affewe 2 ������� 2007 31 ������� 20 sc ������� 2007 "
    print(re.findall('(\d{1,2})\s+(�����(?:�|�)|������(?:�|�)|����(?:�)|�����(?:�|�)|��(?:�|�)|���(?:�|�)|���(?:�|�)|������(?:�)|�������(?:�|�)|������(?:�|�)|�����(?:�|�)|������(?:�|�))\s+(\d{4})', text))
    
