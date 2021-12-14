# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input('Введите число: '))

nn = int(str(n) + str(n))
print(nn)

nnn = int(str(n) + str(n) + str(n))
print(nnn)

print(n + nn + nnn)
