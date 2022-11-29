'''
3) Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

seasons = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите номер месяца от 1 до 12 -  "))
if month ==1 or month == 12 or month == 2:
    print(seasons.get(1))
elif month == 3 or month == 4 or month ==5:
    print(seasons.get(2))
elif month == 6 or month == 7 or month == 8:
    print(seasons.get(3))
elif month == 9 or month == 10 or month == 11:
    print(seasons.get(4))