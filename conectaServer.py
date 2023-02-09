import socket


def conectarAOSerivdor(ip, porta):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((ip,porta))

    return client_socket

