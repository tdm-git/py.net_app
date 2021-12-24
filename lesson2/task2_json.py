import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as file_r:
        data = json.load(file_r)

    with open('orders.json', 'w', encoding='utf-8') as file_w:
        order_data = data['orders']
        order_list = {'item': item,
                      'quantity': quantity,
                      'price': price,
                      'buyer': buyer,
                      'date': date}
        order_data.append(order_list)
        json.dump(data, file_w, indent=4, ensure_ascii=False)


write_order_to_json('принтер', '10', '6700', 'Ivanov I.I.', '24.09.2017')
write_order_to_json('scaner', '20', '10000', 'Petrov P.P.', '11.01.2018')
write_order_to_json('scaner', '20', '10000', 'Petrov P.P.', '11.01.2018')
write_order_to_json('scaner', '20', '10000', 'Petrov P.P.', '11.01.2018')
