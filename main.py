from conectaServer import conectarAOSerivdor




con = conectarAOSerivdor('10.180.44.95', 3005)


def requisicao():

    con.sendall(str.encode("Ola servidor"))
    data = con.recv(1024)

    return data.decode()


print(requisicao())