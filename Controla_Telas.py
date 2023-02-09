from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from TelaCadastro import *
from TelaDepositar import *
from TelaExtrato import *
from TelaLogin import *
from TelaPrincipal import *
from TelaSacar import *
from TelaTransfere import *


from Banco import *


contas_alt = ''
class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)


        self.QtStack = QtWidgets.QStackedLayout()

        self.Tlogin = QtWidgets.QMainWindow()
        self.Tcadastro = QtWidgets.QMainWindow()
        self.Tprinciapal = QtWidgets.QMainWindow()
        self.Tdepositar = QtWidgets.QMainWindow()
        self.TSacar = QtWidgets.QMainWindow()
        self.Ttransfere = QtWidgets.QMainWindow()
        self.Textrato = QtWidgets.QMainWindow()

        self.Login = Ui_TelaLogin()
        self.Login.setupUi(self.Tlogin)

        self.Cadastro = Ui_TelaCadastro()
        self.Cadastro.setupUi(self.Tcadastro)

        self.Principal = Ui_TelaInicial()
        self.Principal.setupUi(self.Tprinciapal)

        self.Depositar = Ui_TelaDepositar()
        self.Depositar.setupUi(self.Tdepositar)

        self.Sacar = Ui_TelaSacar()
        self.Sacar.setupUi(self.TSacar)

        self.Transfere = Ui_TelaTransfere()
        self.Transfere.setupUi(self.Ttransfere)

        self.Extrato = Ui_TelaExtrato()
        self.Extrato.setupUi(self.Textrato)
      
        self.QtStack.addWidget(self.Tlogin)
        self.QtStack.addWidget(self.Tcadastro)
        self.QtStack.addWidget(self.Tprinciapal)
        self.QtStack.addWidget(self.Tdepositar)
        self.QtStack.addWidget(self.TSacar)
        self.QtStack.addWidget(self.Ttransfere)
        self.QtStack.addWidget(self.Textrato)


class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)

        self.bank = Banco()
        self.Login.btn_entrar.clicked.connect(self.BotoaLogin)
        self.Login.btn_criar_conta.clicked.connect(self.BotaoParaTelacriarconta)

        self.Cadastro.btn_cadastrar.clicked.connect(self.BotaoCriar)
        self.Cadastro.btn_voltar.clicked.connect(self.BotaoVoltarParaLogin)

        self.Principal.btn_Depositar.clicked.connect(self.BotaoParaTelaDepositar)
        self.Principal.btn_sacar.clicked.connect(self.BotaoParaTelaSacar)
        self.Principal.btn_transferir.clicked.connect(self.BotaoParaTelaTransferencia)

        self.Principal.btn_extrato.clicked.connect(self.BotaoParaTelaHistorico)
        self.Principal.bnt_sair.clicked.connect(self.BotaoVoltarParaLogin)

        self.Depositar.btn_depositar.clicked.connect(self.BotaoDepositar)
        self.Depositar.btn_voltar.clicked.connect(self.BotaoVoltarParaTelaPrincipal)

        self.Sacar.btn_sacar.clicked.connect(self.BotaoSacar)
        self.Sacar.btn_voltar.clicked.connect(self.BotaoVoltarParaTelaPrincipal)

        self.Transfere.btn_transfere.clicked.connect(self.BotaoTransferir)
        self.Transfere.btn_voltar.clicked.connect(self.BotaoVoltarParaTelaPrincipal)

        self.Extrato.btn_voltar.clicked.connect(self.BotaoVoltarParaTelaPrincipal)
    
    def BotaoParaTelacriarconta(self):
        self.Login.usuario.setText("")
        self.Login.senha.setText("")
        self.QtStack.setCurrentIndex(1)
    
    def BotaoVoltarParaTelaPrincipal(self):
        self.QtStack.setCurrentIndex(2)

    def BotaoVoltarParaLogin(self):
        self.QtStack.setCurrentIndex(0)
    
    def BotaoParaTelaDepositar(self):
        self.QtStack.setCurrentIndex(3)
    
    def BotaoParaTelaSacar(self):
        self.QtStack.setCurrentIndex(4)
    
    def BotaoParaTelaTransferencia(self):
        self.QtStack.setCurrentIndex(5)
    
    def BotaoParaTelaHistorico(self):
        self.QtStack.setCurrentIndex(6)
        self.Extrato.textEdit.setText(f'{(self.bank.conta[contas_alt].extrato())}')
        self.Principal.textEdit.setText(f'{(self.bank.conta[contas_alt].historico.imprime())}')




    @staticmethod
    def botaosair():
        sys.exit(app.exec_())

    def BotoaLogin(self):
        usuario = self.Login.usuario.text()
        cpf = self.Login.senha.text()
        if usuario != '' and cpf != '':
                exite_usuario = self.bank.verificarUser(usuario, cpf)
                print(exite_usuario)
                if exite_usuario == True:
                    global contas_alt
                    contas_alt = cpf
                    self.Login.usuario.setText("")
                    self.Login.senha.setText("")
                    self.Principal.labelNConta.setText(f'{self.bank.conta[contas_alt].numero}')
                    self.Principal.labelSaldo.setText(f'{self.bank.conta[contas_alt].saldo}')
                    
                    self.Principal.nomeUser.setText(f'{usuario}')
                    self.QtStack.setCurrentIndex(2)
                else:
                    QMessageBox.information(None, 'Banco', "Usuario não exite.")               
        else:
                self.Login.usuario.setText("")
                self.Login.senha.setText("")
                QMessageBox.information(None, 'Banco', "Todos os espaços devem estar preenchidos.")


    def BotaoCriar(self):
        nome = self.Cadastro.Criar_Nome.text()
        sobrenome = self.Cadastro.CriarSobreNM.text()
        cpf = self.Cadastro.criar_cpf.text()
        usuario = self.Cadastro.criar_usuario.text()
        senha = self.Cadastro.criar_senha.text()

        if nome != '' and sobrenome != '' and cpf != '' and usuario != '' and senha != '':
                if self.bank.addConta(nome,sobrenome,cpf,usuario, senha):
                    self.Cadastro.Criar_Nome.setText("")
                    self.Cadastro.CriarSobreNM.setText("")
                    self.Cadastro.criar_cpf.setText("")
                    self.Cadastro.criar_usuario.setText("")
                    self.Cadastro.criar_senha.setText("")
                    QMessageBox.information(None, 'Banco', "Dados cadastrados com sucesso.")
                else:
                    QMessageBox.information(None, 'Banco', "Não foi possivel realizar o cadastro")

        else:
            self.Cadastro.Criar_Nome.setText("")
            self.Cadastro.CriarSobreNM.setText("")
            self.Cadastro.criar_cpf.setText("")
            self.Cadastro.criar_usuario.setText("")
            self.Cadastro.criar_senha.setText("")
           
        

    
    def BotaoDepositar(self):
        valor = self.Depositar.valor_depositar.text()
        if valor != '':
        #    self.bank.conta[dest].deposita(float(valor))
            valor = float(valor)    
            if self.bank.conta[contas_alt].deposita(valor):
                self.Depositar.valor_depositar.setText("")         
                self.Principal.labelSaldo.setText(f'{self.bank.conta[contas_alt].saldo}')
                self.Extrato.textEdit.setText(f'{(self.bank.conta[contas_alt].extrato())}')
                self.Principal.textEdit.setText(str(self.bank.conta[contas_alt].historico.imprime()))

            else:

                self.Depositar.valor_depositar.setText("")   

        else:
  
            self.Depositar.valor_depositar.setText("")   


    def BotaoSacar(self):
        valor = self.Sacar.valor_Sacar.text()
        valor = float(valor)
        if valor != '':
            if self.bank.conta[contas_alt].sacar(valor):
                self.Principal.labelSaldo.setText(f'{self.bank.conta[contas_alt].saldo}')
                self.Extrato.textEdit.setText(f'{(self.bank.conta[contas_alt].extrato())}')
                self.Principal.textEdit.setText(str(self.bank.conta[contas_alt].historico.imprime()))
                self.Sacar.valor_Sacar.setText('')
                QMessageBox.information(None, 'Saque realizado com sucesso')
            else:
                QMessageBox.information(None, 'Não foi possivel realizar o saque')

                

    def BotaoTransferir(self):
        num = self.Transfere.cpfDestino.text()
        valor = self.Transfere.valorTransfere.text()
        if num != '' and valor != '':
                valorA = int(num)
                n = self.bank.busca_conta(valorA)
                if n != False:
                    valorb = float(valor)
                    self.bank.conta[contas_alt].transfere(contas_alt,valorb, n)

                    self.Principal.labelSaldo.setText(f'{self.bank.conta[contas_alt].saldo}')
                    self.Extrato.textEdit.setText(f'{(self.bank.conta[contas_alt].extrato())}')
                    self.Principal.textEdit.setText(str(self.bank.conta[contas_alt].historico.imprime()))
                    self.Transfere.valorTransfere.setText('')
                else:
                    self.Transfere.valorTransfere.setText('')

        else:
            self.Transfere.valorTransfere.setText('')
            QMessageBox.information(None, 'Transferência', "Necessário preencher todos os campos!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())