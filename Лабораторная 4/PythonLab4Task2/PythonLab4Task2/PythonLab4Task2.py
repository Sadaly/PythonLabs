# -*- coding:cp1251 -*-

import re
from collections import Counter

def find_common_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        sentences = re.split(r'[.!?]', text)
    
        common_words = Counter()
        
        for sentence in sentences:
            words = re.findall(r'\b\w+\b', sentence.lower())  # Игнорируем регистр
            common_words.update(words)
    

        for word, count in common_words.items():
            if count == len(sentences) - 1:
                return word
    
        return "Слово, встречающееся в каждом предложении, не найдено."


file_path = '1.txt'
print(find_common_word(file_path))

