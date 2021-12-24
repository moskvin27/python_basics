# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

# решение через list:
month_number = int(input('Введите месяц в виде целого числа от 1 до 12: '))

month_list = list(range(1, 13))

if month_number in month_list[0:2] or month_number == month_list[11]:
    print('На дворе зима!')
elif month_number in month_list[2:5]:
    print('Наступила весна!')
elif month_number in month_list[5:8]:
    print('Наконец-то лето!')
elif month_number in month_list[8:11]:
    print('Осенняя пора..')
else:
    print('error: Введен параметр вне заданного диапозона')



