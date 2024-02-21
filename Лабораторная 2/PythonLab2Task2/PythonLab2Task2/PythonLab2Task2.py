# -*- coding:cp1251 -*-
class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.children = []

def build_genealogical_tree(N, relationships):
    # Создаем словарь, где ключи - имена, значения - объекты Person
    people_dict = {"root": Person("root", 0)}
    
    # Заполняем словарь и создаем связи родителя с детьми
    for child, parent in relationships:
        if parent not in people_dict:
            people_dict[parent] = Person(parent, +1)
        if child not in people_dict:
            people_dict[child] = Person(child, +1)
        people_dict[child].height = people_dict[parent].height - 1
        people_dict[parent].children.append(people_dict[child])
        
    sorted_names = sorted(people_dict.keys())
    
    # Выводим имена и высоты в лексикографическом порядке
    correct_height = -1 * min(person.height for person in people_dict.values())
    for name in sorted_names:
        if (name != "root"):
            print(f"{name} {people_dict[name].height + correct_height}")


N = int(input("Введите количество элементов в генеалогическом древе (N): "))
relationships = [input().split() for i in range(N - 1)]

build_genealogical_tree(N, relationships)
