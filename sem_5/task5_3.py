'''
3) Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк). Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''

with open('test_3.txt', 'r') as my_file:
    summa = 0
    count = 0
    persons = []
    for line in my_file:
        tokens = line.split(' ')
        if float(tokens[1]) < 20000:
            persons.append(tokens[0])
        summa += float(tokens[1])
        count += 1
result = summa / count
print(f"Фамилии сотрудников - {persons}")
print(f"Средняя з/п - {result}")

