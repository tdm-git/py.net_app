"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

site_list = ['yandex.ru', 'youtube.ru']

for str_site in site_list:
    result = subprocess.Popen(['ping', str_site], stdout=subprocess.PIPE)
    for line_out in result.stdout:
        suffix = chardet.detect(line_out)['encoding']
        # print(line_out.decode(suffix))  - так тоже работает, но по условиям принудительно в киррилицу поэтому:
        print(line_out.decode(suffix).encode('utf-8').decode('utf-8') )
