import re
import csv


def get_data():
    first_line = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for f_name in ('info_1.txt', 'info_2.txt', 'info_3.txt'):
        file_obj = open(f_name, encoding='utf-8')
        file_text = file_obj.read()

        os_prod_reg = re.compile(r'Изготовитель системы:.*')
        os_prod_list.append(os_prod_reg.findall(file_text)[0].split(sep=':')[1].strip())
        os_name_reg = re.compile(r'Название ОС:.*')
        os_name_list.append(os_name_reg.findall(file_text)[0].split(sep=':')[1].strip())
        os_code_reg = re.compile(r'Код продукта:.*')
        os_code_list.append(os_code_reg.findall(file_text)[0].split(sep=':')[1].strip())
        os_type_reg = re.compile(r'Тип системы:.*')
        os_type_list.append(os_type_reg.findall(file_text)[0].split(sep=':')[1].strip())

    main_data = [first_line] + \
                [[i,j,q,g,h] for i,j,q,g,h in zip(range(1,4), os_prod_list, os_name_list, os_code_list, os_type_list)]
    return main_data

def write_to_csv(out_file):
    main_data = get_data()
    with open(out_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in main_data:
            writer.writerow(row)

write_to_csv('result.csv')
