# -*- coding:cp1251 -*-
class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.children = []

def build_genealogical_tree(N, relationships):
    # ������� �������, ��� ����� - �����, �������� - ������� Person
    people_dict = {"root": Person("root", 0)}
    
    # ��������� ������� � ������� ����� �������� � ������
    for child, parent in relationships:
        if parent not in people_dict:
            people_dict[parent] = Person(parent, +1)
        if child not in people_dict:
            people_dict[child] = Person(child, +1)
        people_dict[child].height = people_dict[parent].height - 1
        people_dict[parent].children.append(people_dict[child])
        
    sorted_names = sorted(people_dict.keys())
    
    # ������� ����� � ������ � ������������������ �������
    correct_height = -1 * min(person.height for person in people_dict.values())
    for name in sorted_names:
        if (name != "root"):
            print(f"{name} {people_dict[name].height + correct_height}")


N = int(input("������� ���������� ��������� � ��������������� ����� (N): "))
relationships = [input().split() for i in range(N - 1)]

build_genealogical_tree(N, relationships)
