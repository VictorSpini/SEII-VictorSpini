# Victor Spini Paranaiba - 11611EMT005

import argparse
import os
import socket
import sys
import tqdm

host = 'localhost'
backlog = 5
BUFFER_SIZE = 1024
SEPARAR = "<SEPARAR>"

def funcao_servidor(port, filename):
    # Cria a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Permitir reutilização de endereço / porta
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Liga o socket à porta
    server_address = (host, port)
    print("Iniciando servidor em %s port %s" % server_address)
    sock.bind(server_address)

    # Ouça os clientes, o argumento de lista de pendências especifica o número máximo de conexões em fila
    sock.listen(backlog)
    client_socket, address = sock.accept()
    print(f"Conectando ao {address}")

    # receber usando o socket do cliente, não o socket do servidor
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename_input, filesize = received.split(SEPARAR)
    # remove o caminho absoluto se houver, converter para inteiro
    filesize = int(filesize)
    # comece a receber o arquivo do socket e escrever no fluxo de arquivos
    progress = tqdm.tqdm(range(filesize),f"Receiving {filename}",unit="B",unit_scale=True,unit_divisor=1024)
    with open(filename, "wb") as f:
        while True:
            # ler 1024 bytes do socket (receive)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                # a transmissão do arquivo está concluída
                break
            # escreva no arquivo os bytes que acabamos de receber e atualize a barra de progresso
            f.write(bytes_read)
            progress.update(len(bytes_read))

    # fecha o client socket
    client_socket.close()
    # fecha o server socket
    sock.close()
    # fim de conexão


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    parser.add_argument('--filename',action="store",dest="filename",type=str,required=True)
    given_args = parser.parse_args()
    port = given_args.port
    filename = given_args.filename

    funcao_servidor(port, filename)
