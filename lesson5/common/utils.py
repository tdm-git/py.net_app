import json
from common.settings import MAX_PACKAGE_LENGTH, ENCODING

def get_message(client):

    new_message = client.recv(MAX_PACKAGE_LENGTH)  # получили ответ
    json_message = new_message.decode(ENCODING)    # декодировали байты в строку
    return json.loads(json_message)                # возвращаем словарь


def send_message(sock, message):

    new_message = json.dumps(message)        # преобразуем словать в строку
    sock.send(new_message.encode(ENCODING))  # кодируем и отправляем в сокет
