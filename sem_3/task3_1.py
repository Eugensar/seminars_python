'''
1) Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
'''

def my_func (x, y):
    if y != 0:
        return x / y
    else:
        print("На ноль не делить!!!")

print(my_func(int(input("Введите первое число - ")), int(input("Введите второе число - "))))