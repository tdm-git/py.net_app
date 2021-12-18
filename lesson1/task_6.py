"""
Задание 6.

Создать  НЕ программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».

Принудительно программно открыть файл в формате Unicode и вывести его содержимое.
Что это значит? Это значит, что при чтении файла вы должны явно указать кодировку utf-8
и файл должен открыться у ЛЮБОГО!!! человека при запуске вашего скрипта.

При сдаче задания в папке должен лежать текстовый файл!

Это значит вы должны предусмотреть случай, что вы по дефолту записали файл в cp1251,
а прочитать пытаетесь в utf-8.

Преподаватель будет запускать ваш скрипт и ошибок НЕ ДОЛЖНО появиться!

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке
но открыть нужно ИМЕННО!!! в формате Unicode (utf-8)
--- обратите внимание на чтение файла в режиме rb
для последующей переконвертации в нужную кодировку

НАРУШЕНИЕ обозначенных условий - задание не выполнено!!!
"""
import chardet

def make_file(name, text):
    with open(name, 'w') as file:
        for file_line in text:
            file.write(f'{file_line}\n')
    file.close()

def convert_file(name):
    with open(name, 'rb') as file:
        file_text = file.read()
    suffix = chardet.detect(file_text)['encoding']
    with open(name, 'w', encoding='utf-8') as file:
        file.write(file_text.decode(suffix))

def print_file(name):
    with open(name, 'r', encoding='utf-8') as file:
        print(file.read())


words_list = ['сетевое программирование', 'сокет', 'декоратор']
file_name = 'test_file.txt'

make_file(file_name, words_list)
convert_file(file_name)
print_file(file_name)
