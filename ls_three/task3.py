# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    sum1, sum2, sum3 = a + b, a + c, b + c
    return max(sum1, sum2, sum3)

a = int(input('Введите значение "а": '))
b = int(input('Введите значение "b": '))
c = int(input('Введите значение "c": '))

print(my_func(a, b, c))

''' Является ли такое решение удовлетворяющим условию "принимает позиционные аргументы" ? '''
# def my_func():
#     a = int(input('Введите значение "а": '))
#     b = int(input('Введите значение "b": '))
#     c = int(input('Введите значение "c": '))
#
#     sum1, sum2, sum3 = a + b, a + c, b + c
#
#     return max(sum1, sum2, sum3)
#
#
# print(my_func())
