# итератор, повторяющий элементы некоторого списка, определённого заранее.

from itertools import cycle


def script():
    a = int(input('Введите количесвто повторений элемента списка: '))
    с = 0
    my_list = [1, 2, 3, 4, 5]
    for i in cycle(my_list):
        if с >= a:
            break
        print(i)
        с += 1


script()
