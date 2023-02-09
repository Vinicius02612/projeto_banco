import mysql.connector


class DataBase:

    def __init__(self, host, users, passW, nameDB):
        self.conexao = mysql.connector.connect(host=host, user=users, password=passW, database=nameDB)
        self.cursor = self.conexao.cursor()
        
    def CadastraCliente(self, nome, sobrenome, cpf):
        try:
            dados = (nome,sobrenome,cpf)
            sql = "INSERT INTO Cliente (nome, sobrenome, cpf) VALUES (%s, %s, %s)"
            self.cursor.execute(sql,dados)
            self.conexao.commit()
            return True
        except:
            return False, 'Não foi possivel inserir os dados'


    def BuscarCliente(self, cpf):
        try:
            sql = f"SELECT * FROM Cliente WHERE cpf={cpf}"
            self.cursor.execute(sql)
            return list(self.cursor)
        except:
            return False, 'Usuario não encontrado'

    
    def  InserirConta(self, numero,saldo,senha,id_usuario):

        try:
            dados = (numero, senha, id_usuario)
            sql = "INSERT INTO Conta (numero,saldo,senha,Cliente_IdCliente ) VALUES (%s, %s, %s,%s)"
         #   sql = f"INSERT INTO  Conta (numero,saldo,senha, Cliente_IdCliente) VALUES ({numero},{0.00},{senha},{id_usuario})"
            self.cursor.execute(sql,dados)
            self.conexao.commit()
            return True
        except:
            return False


    def BuscarConta(self, idusuario):
        try:
            id_usuario = int(idusuario)
            sql = f"SELECT * FROM Conta WHERE Cliente_IdCliente = {id_usuario}"
            self.cursor.execute()
            return True
        except:
            return False

    def BuscarId(self, cpf):
        sql = f"SELECT IdCliente FROM Cliente WHERE cpf = {cpf}"
        self.cursor.execute(sql)
        retrono_id = self.cursor.fetchone()
        return retrono_id[0]




    

