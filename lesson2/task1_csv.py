import csv


def get_list_from_file(file_name:str, name_list:list):
    result = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            line_list = line.split(sep=':')
            if line_list[0] in name_list:
                result.append(line_list[1].strip())
    return result

def get_data(file_list, import_list):
    result = []
    result.append(import_list)
    for i in file_list:
        result.append(get_list_from_file(i, import_list))
    return result

def write_to_csv(file_name, file_list, import_list):
    main_data = get_data(file_list, import_list)
    with open('main_data.csv', 'w', encoding='utf-8') as file:
        f_n_writer = csv.writer(file)
        for row in main_data:
            f_n_writer.writerow(row)


file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
import_list = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']

write_to_csv('main_data.csv', file_list, import_list)
