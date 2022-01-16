import sys
import socket
import time
from common.settings import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, DEFAULT_ADDRESS, DEFAULT_PORT
from common.utils import get_message, send_message


def presence_to_server(user_name='Guest'):
    # формируем приглашение и список обязательных полей
    new_message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: user_name
        }
    }
    return new_message


def check_answer(message):
    # проверяем сообщение
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():

    try:
        server_address = sys.argv[2]
        server_port = int(sys.argv[3])
    except IndexError:
        server_address = DEFAULT_ADDRESS
        server_port = DEFAULT_PORT

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    send_message(transport, presence_to_server())
    server_answer = check_answer(get_message(transport))
    print(server_answer)


if __name__ == '__main__':
    main()
