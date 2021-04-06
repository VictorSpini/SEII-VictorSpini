# Victor Spini Paranaiba - 11611EMT005

import argparse
import socket
from threading import Thread

SERVER_HOST = 'localhost'
SEPARAR_TOKEN = "<SEPARAR>"

def servidor(port):
    SERVER_PORT = port
    # inicializar a lista / conjunto de todos os soquetes do cliente conectado
    client_sockets = set()
    # create a TCP socket
    socket = socket.socket()
    # tornar a porta uma porta reutilizável
    socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # ligar o socket ao endereço que especificamos
    socket.bind((SERVER_HOST, SERVER_PORT))
    # escute as próximas conexões
    socket.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    def listen_for_client(cs):
        """
        Esta função continua ouvindo uma mensagem do socket `cs`
        Sempre que uma mensagem for recebida, transmita-a para todos os outros clientes conectados
        """
        while True:
            try:
                # continue ouvindo por uma mensagem do socket `cs`
                msg = cs.recv(1024).decode()
            except Exception as e:
                # cliente não está mais conectado
                # remova-o do conjunto
                print(f"[!] Error: {e}")
                client_sockets.remove(cs)
            else:
                # se recebemos uma mensagem, substitua o <SEP>
                msg = msg.replace(SEPARAR_TOKEN, ": ")
            # iterar sobre todos os sockets conectados
            for client_socket in client_sockets:
                # e envia a msg
                client_socket.send(msg.encode())

    while True:
        # continua atentos a novas conexões o tempo todo
        client_socket, client_address = socket.accept()
        print(f"[+] {client_address} connected.")
        # adicione o novo cliente conectado aos sockets conectados
        client_sockets.add(client_socket)
        # inicie um novo tópico que ouça as mensagens de cada cliente
        thread = Thread(target=listen_for_client, args=(client_socket,))
        # faz o thread daemon para que ele termine sempre que o thread principal terminar
        thread.daemon = True
        # inicia a thread
        thread.start()
    # fecha client sockets
    for cs in client_sockets:
        cs.close()
    # fecha servidor socket
    socket.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server')
    parser.add_argument('--port',action="store",dest="port",type=int,required=True)
    given_args = parser.parse_args()
    port = given_args.port
    servidor(port)
