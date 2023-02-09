import socket

import threading


class Serividor:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))

    def InciarConexao(self):
     
        while True:
            self.server.listen(1080)
            print("Aguardando conexão...")
            # servidor aguardando conexao
            client_sock, client_address = self.server.accept()
            print(f'{client_address[0]} conectado')
            client_sock.sendall((str.encode("Ola amigo tudo bem? ")))
            # criar thread para a conexao
            #new_thread = ClienteTH(client_sock, client_address)
            # iniciar a thread
            #new_thread.Executar()


if __name__ == "__main__":
    server = Serividor('127.0.0.1', 8000)
    server.InciarConexao()



