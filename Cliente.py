from Pessoa import Pessoa


# classe Cliente que extende de pessoa, porem com atribibutos de usuario e senha
class Cliente(Pessoa):

    __slot__ = ['nome', 'sobrenome', 'cpf']

    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        


    @property
    def nome(self):
        return super().nome
    
    @nome.setter
    def nome(self, nome):
        self._sobrenome = nome
        return self.nome

    @property
    def sobrenome(self):
        return super().sobrenome
    
    @sobrenome.setter
    def sobrenome(self, sbnome):
        self._sobrenome = sbnome
        return self._sobrenome
    
    @property
    def cpf(self):
        return super().cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
        return self._cpf



    def get_dados(self):
        return super().get_dados()
   
   
    
    def verificarCPF(self, cpf):
        if cpf == self._titular.cpf:
            return True
        else:
            return False
    
    def __str__(self):
        return f'nome: {self._nome},sobrenome: {self._sobrenome},cpf: {self._cpf}'
