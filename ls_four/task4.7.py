# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

factorial = int(input('От какого числа получить факториал? '))
count_fact = int(input('Сколько элементов вывести на экран?'))


def fuct(factorial):
    my_list = list(range(1, factorial + 1))

    element_fuct = 1
    for i in my_list:
        element_fuct *= i
        yield element_fuct


for number, el in enumerate(fuct(factorial), 1):
    if number > count_fact:
        break
    print(number, el, sep=') ')


