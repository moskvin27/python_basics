# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

# решение через dict:
number = int(input('Введите месяц в виде целого числа от 1 до 12: '))

month_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
season_len = list(range(1, 13))

for season, month in month_dict.items():
    if number in month:
        print(f'Сейчас {season}')
    elif number not in season_len:
        print('error: Введен параметр вне заданного диапозона')
        break







