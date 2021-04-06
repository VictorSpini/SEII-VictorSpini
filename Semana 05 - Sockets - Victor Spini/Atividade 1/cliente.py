# Victor Spini Parnaiba - 11611EMT005

import argparse
import os
import socket
import tqdm

SEPARAR = "<SEPARAR>"
host = 'localhost'
BUFFER_SIZE = 1024  # envia 4096 bytes a cada passo de tempo

def funcao_cliente(port, filename):
    filesize = os.path.getsize(filename)
    # Cria a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecte o socket ao servidor
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    sock.connect(server_address)

    try:
        # Enviar dados
        sock.send(f"{filename}{SEPARAR}{filesize}".encode())
        progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "rb") as f:
            while True:
                # leia os bytes do arquivo
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    # a transmissão do arquivo está concluída
                    break
                # usamos sendall para garantir a transmissão em redes ocupadas
                sock.sendall(bytes_read)
                # atualize a barra de progresso
                progress.update(len(bytes_read))
        # fecha o socket
        sock.close()
        # Procura resposta

    except socket.error as e:
        print("Socket error: %s" % str(e))

    except Exception as e:
        print("Outra exceção: %s" % str(e))

    finally:
        print("Fechando a conexão com o servidor")
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Client')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    parser.add_argument('--filename', action="store", dest="filename", type=str, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    filename = given_args.filename
    funcao_cliente(port, filename)
