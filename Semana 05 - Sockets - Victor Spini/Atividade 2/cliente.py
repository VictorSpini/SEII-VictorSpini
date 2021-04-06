# Victor Spini Paranaiba 11611EMT005

import argparse
import socket
from datetime import datetime
from threading import Thread

SEPARAR_TOKEN = "<SEPARAR>"
init()

def cliente(port, host, name):
    SERVER_HOST = host
    SERVER_PORT = port  # server's port
    # inicialização do TCP socket
    socket = socket.socket()
    print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
    # conecta com o server
    socket.connect((SERVER_HOST, SERVER_PORT))
    print("[+] Connected.")

    def listen_for_messages():
        while True:
            message = socket.recv(1024).decode()
            print("\n" + message)
    # faz um tópico que ouça as mensagens para este cliente e as imprima
    thread = Thread(target=listen_for_messages)
    # faz com que o thread daemon para que ele termine sempre que o thread principal terminar
    thread.daemon = True
    # inicia a thread
    thread.start()

    while True:
        # mensagem de entrada que queremos enviar para o servidor
        to_send = input()
        # uma maneira de sair do programa
        if to_send.lower() == 'q':
            break
        # adicione a data e hora, nome do remetente
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        to_send = f"[{date_now}] {name}{SEPARAR_TOKEN}{to_send}"
        # finalmente, manda a mensagem
        socket.send(to_send.encode())

    # close the socket
    socket.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Client')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    parser.add_argument('--host', action="store", dest="host", type=str, required=True)
    parser.add_argument('--name', action="store", dest="name", type=str, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    host = given_args.host
    name = given_args.name
    cliente(port, host, name)
