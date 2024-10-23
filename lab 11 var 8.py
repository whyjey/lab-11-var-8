import csv
import random

# Читання питань з CSV файлу
with open('quest.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    questions = [row[0] for row in reader]  # Припускаємо, що питання в першому стовпці

# Перемішування питань у випадковому порядку
random.shuffle(questions)

# Виведення питань
for question in questions:
    print(question)
import json
from collections import defaultdict

# Читання тексту з файлу
with open('book_fragment.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Видалення небажаних символів та розбиття тексту на слова
words = text.split()

# Підрахунок кількості слів за їх довжиною
word_length_count = defaultdict(int)
for word in words:
    cleaned_word = ''.join(filter(str.isalpha, word))  # Видаляємо знаки пунктуації
    word_length = len(cleaned_word)
    if word_length > 0:  # Ігноруємо порожні слова
        word_length_count[word_length] += 1

# Запис результатів у JSON файл
with open('word_lengths.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(word_length_count, jsonfile, indent=4)

print("Результати збережені у файл word_lengths.json")
