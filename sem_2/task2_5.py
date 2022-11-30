'''
5) Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент
рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например,
my_list = [7, 5, 3, 3, 2].
'''

number = int(input("Введите число - "))
my_list = [7, 5, 3, 3, 2]
for element in my_list:
    if my_list.count(number) > 0:
        my_list.insert(my_list.index(number) + my_list.count(number), number)
        break
    else:
        if number > element:
            my_list.insert(my_list.index(element), number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)