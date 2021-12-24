import yaml

# исходный файл
with open('file.yaml', 'r', encoding='utf-8') as f_n:
    yaml_file = yaml.load(f_n, Loader=yaml.SafeLoader)
# новый файл
yaml_data = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
           'items_quantity': 4,
           'items_ptice': {'computer': '200\u20ac-1000\u20ac',
                           'printer': '100\u20ac-300\u20ac',
                           'keyboard': '5\u20ac-50\u20ac',
                           'mouse': '4\u20ac-7\u20ac'}
           }
with open('file2.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(yaml_data, file, default_flow_style=False, allow_unicode=True
)

print(f'результат сравнения файлов - {yaml_file == yaml_data}')
