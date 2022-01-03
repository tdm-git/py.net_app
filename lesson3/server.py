import socket
import sys
from common.settings import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, PRESENCE, TIME, USER, ERROR, DEFAULT_PORT
from common.utils import get_message, send_message


def check_message(message):

    if (ACTION in message and message[ACTION] == PRESENCE) and \
       (USER in message and message[USER][ACCOUNT_NAME] == 'Guest') and \
       TIME in message:
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():

    if '-a' in sys.argv:
        client_address = sys.argv[sys.argv.index('-a') + 1]
    else:
        client_address = ''

    if '-p' in sys.argv:
        client_port = int(sys.argv[sys.argv.index('-p') + 1])
    else:
        client_port = DEFAULT_PORT

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((client_address, client_port))
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        cient_message = get_message(client)
        response = check_message(cient_message)
        send_message(client, response)
        client.close()


if __name__ == '__main__':
    main()
