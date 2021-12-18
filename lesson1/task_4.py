"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
result_list = ['разработка', 'администрирование', 'protocol', 'standard']

for i in result_list:
    i_encode = i.encode('utf-8')
    i_decode = i_encode.decode('utf-8')
    print(f'{i} -> {i_encode} -> {i_decode}')
