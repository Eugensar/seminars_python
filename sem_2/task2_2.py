'''
2) Для списка реализовать обмен значений соседних элементов, т.е. значениями
обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
'''

new_list = [int(value) for value in input("Введите числа через пробел - ").split()]
el = 0
for i in range(int(len(new_list)/2)):
   new_list[el], new_list[el + 1] = new_list[el + 1], new_list[el]
   el += 2
print(new_list)