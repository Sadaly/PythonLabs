# -*- coding:cp1251 -*-

import re

def is_valid_email(email):
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(re.match(email_pattern, email))

def get_valid_email(email):
    if is_valid_email(email):
        return email
    else:
        raise ValueError("Некорректный адрес электронной почты")

# Пример использования
try:
    user_input = input("Введите адрес электронной почты: ")
    valid_email = get_valid_email(user_input)
    print(f"Введенный адрес электронной почты: {valid_email}")
except ValueError as e:
    print(e)

     