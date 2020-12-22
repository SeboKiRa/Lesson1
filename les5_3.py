'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

import os

file_path = os.path.join(os.path.dirname(__file__), 'work3.txt')

salary = 0       # Оклад
count = 0        # Переменная для подсчета кол-ва сотрудников
persons = []     # Список сотрудников
with open(file_path, 'r', encoding='UTF-8') as file:
    for line in file:
        print(line, end="")
        tokens = line.split(':')
        if float(tokens[1]) <= 20000:
            persons.append(tokens[0])
        salary += float(tokens[1])
        count += 1
print(f"\nСписок сотрудников, с окладом менее 20000 руб.: {', '.join(persons)}")
print(f"Средняя величина дохода сотрудников: {salary / count:.2f}")
