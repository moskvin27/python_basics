# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

my_file = open('my_file2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')

my_file = open('my_file2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Строка № {i + 1}. Количество символов: {len(content[i])}')

my_file.close()
