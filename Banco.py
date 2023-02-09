from bd_mysql import *
from Conta import *
from Cliente import Cliente


import random



class Banco:

    __slot__ = {'_database'}

    def __init__(self):
        self._database = DataBase('localhost', 'root', 'vini123@77','banco')


    @property
    def conta(self):
        return self._contas
    
    @conta.setter
    def conta(self, conta):
        self._contas = conta
    
    #adicionando clientes no dicionarios de clientes e criando a conta
    def addConta(self, nome, sobrenome,cpf,usuario,senha):
        cliente = Cliente(nome, sobrenome,cpf)
        numero_conta = random.randint(000,999)
        conta = Conta(numero_conta,cliente,usuario,senha)

        # verifico se o cliente ja esta cadastrado no banco
        usuario = self._database.BuscarCliente(cliente.cpf)
        print("Retorno de usuario: ", usuario)

        if not usuario:# se o usuario não for encotrado
            #cadastra o cliente no banco de  dados
            self._database.CadastraCliente(cliente.nome,cliente.sobrenome,cliente.cpf)

            id_usuario = self._database.BuscarId(cliente.cpf)
            print(id_usuario)
            self._database.InserirConta(numero_conta,0.00,senha,id_usuario)


            # apos cadastrar o cliente, criar conta do usuario
            #       self._database.InserirConta(conta.numero,conta.saldo,conta.senha,id_usuario[0][0])
            return True

    


 
    def verificarnum(self, num):
        for n in self._contas.values():
            if n == num:
                return num
                
        return False
    
    def busca_conta(self, num):
        
        for i in self._contas.keys():
            if self._contas[i].numero == num:
                return self._contas[i]
        return False
    
    def verificarUser(self, usuario, cpf):
        for chave in self._clientes.keys():
            for ch in self._contas.keys():
                if self._contas[ch].usuario == usuario and self._clientes[chave].cpf == cpf:
                    return True
        return False

    def mostrarDados(self):
        for chave, x in self._clientes.items():
            print(f'{chave}| {x}')
        for j , y in self._contas.items():
            print(f'{j}| {y}')



   


  



