import datetime

class Historico:

    def __init__(self) -> None:
        self.data_abertura = datetime.datetime.today()
        self.transacao = []

    def imprime(self):
        print(f'Data de transacão {self.data_abertura}')
        print('Transação => ')
        for i in self.transacao:
            print(i) 

    
    def __str__(self) -> str:
        return  f'{self.data_abertura}\n{self.transacao}'



class Conta:
    _total_contas = 0

    __slot__ = ['_numero', '_cliente', '_saldo','usuario','_historico','senha','limite']
    
    def __init__(self,numero,cliente, usuario, senha,saldo = 0.0, limite = 2000):
        self._numero = numero
        self._titular = cliente
        self._saldo =saldo
        self._usuario = usuario
        self._historico = Historico()
        self._senha = senha
        self._limite = limite
        
        Conta._total_contas += 1 
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero
        return self._numero
    

    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, ttl):
        self._titular = ttl
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, sld):
        if self._saldo < 0:
            return 'saldo não pode ser negativo'
        else: 
            self._saldo = sld
    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, lmt):
        self._limite = lmt
        return self._limite

    @property
    def usuario(self):
        return self._usuario
    
    @usuario.setter
    def usuario(self,user):
        self._usuario = user
    
    
    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self,passw):
        self._senha = passw

    @property
    def historico(self):
        return self._historico

    @historico.setter
    def set_historico(self,h):
        self._historico = h


    
    def verificarUser(self, usuario):
        if self._usuario == usuario:
            return True,usuario
        else:
            return False
    
    def verificarSenha(self, senha):
        if self._senha == senha:
            return True
        else:
            return False
    
    def verificarCPF(self, cpf):
        if cpf == self._titular.cpf:
            return True
        else:
            return False

    def verificarNumero(self, numero):
        if numero == self._numero:
            return True
        else:
            return False
        



    def deposita(self, valor):
        if valor < self._limite:
            self._saldo += valor
            self._historico.transacao.append(f'{datetime.datetime.now()} - Deposito de {valor}  ')
            return True,'Deposito realizado com sucesso'
        return False, 'valor de deposito não pode eceder o limite'
    
    def sacar(self, valor):
        if valor > self._saldo:
            return False,'Impossivel relaixar o saque'
        self._saldo -= valor
        self._historico.transacao.append(f'{datetime.datetime.now()} - Saque de {valor} ')
        return True
    
    def transfere(self, cpfatual,valor, destino):
        if self._titular.cpf == cpfatual and self._saldo > 0.0:
            self._saldo -= valor
            destino.deposita(valor)
            self.historico.transacao.append(f'{datetime.datetime.now()}Transferencia de {valor}  ')
            return True
        else:
            return False

    def pega_dados(self):
        return f'Numero:{self._numero}, Titular:{self._titular}, Saldo:{self._saldo},Usuario:{self._usuario},Senha:{self._senha}'

    
    def extrato(self):
        print(f'Conta:{self._numero}  Saldo:{self.saldo}')
        return self._historico.transacao.append(f'Pedido de Extrato em: {datetime.datetime.now()}')

    def get_historico(self):
        return f'{self._historico.imprime()}'

    @staticmethod
    def get_total_contas():
        return Conta._total_contas


    def __str__(self):
        return f'\nNumero:{self._numero}, Titular:{self._titular}, Saldo:{self._saldo},Usuario:{self._usuario},Senha:{self._senha}\n'
        




