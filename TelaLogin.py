# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaLogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaLogin(object):
    def setupUi(self, TelaLogin):
        TelaLogin.setObjectName("TelaLogin")
        TelaLogin.resize(478, 600)
        TelaLogin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(TelaLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 451, 561))
        self.widget.setObjectName("widget")
        self.user = QtWidgets.QLabel(self.widget)
        self.user.setGeometry(QtCore.QRect(80, 90, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.user.setFont(font)
        self.user.setStyleSheet("color: rgb(192, 97, 203);")
        self.user.setObjectName("user")
        self.passWord = QtWidgets.QLabel(self.widget)
        self.passWord.setGeometry(QtCore.QRect(80, 190, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.passWord.setFont(font)
        self.passWord.setStyleSheet("color: rgb(192, 97, 203);")
        self.passWord.setObjectName("passWord")
        self.usuario = QtWidgets.QLineEdit(self.widget)
        self.usuario.setGeometry(QtCore.QRect(80, 120, 301, 41))
        self.usuario.setStyleSheet("border-color: rgb(192, 97, 203);\n"
"color: rgb(145, 65, 172);")
        self.usuario.setObjectName("usuario")
        self.senha = QtWidgets.QLineEdit(self.widget)
        self.senha.setGeometry(QtCore.QRect(80, 220, 301, 41))
        self.senha.setStyleSheet("color: rgb(145, 65, 172);")
        self.senha.setObjectName("senha")
        self.btn_entrar = QtWidgets.QPushButton(self.widget)
        self.btn_entrar.setGeometry(QtCore.QRect(160, 300, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_entrar.setFont(font)
        self.btn_entrar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(145, 65, 172);")
        self.btn_entrar.setObjectName("btn_entrar")
        self.no_conta = QtWidgets.QLabel(self.widget)
        self.no_conta.setGeometry(QtCore.QRect(40, 390, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.no_conta.setFont(font)
        self.no_conta.setStyleSheet("color: rgb(192, 97, 203);\n"
"color: rgb(145, 65, 172);")
        self.no_conta.setObjectName("no_conta")
        self.btn_criar_conta = QtWidgets.QPushButton(self.widget)
        self.btn_criar_conta.setGeometry(QtCore.QRect(230, 380, 201, 31))
        self.btn_criar_conta.setStyleSheet("color: rgb(129, 61, 156);")
        self.btn_criar_conta.setObjectName("btn_criar_conta")
        self.user_2 = QtWidgets.QLabel(self.widget)
        self.user_2.setGeometry(QtCore.QRect(200, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.user_2.setFont(font)
        self.user_2.setStyleSheet("color: rgb(192, 97, 203);")
        self.user_2.setObjectName("user_2")
        TelaLogin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TelaLogin)
        self.statusbar.setObjectName("statusbar")
        TelaLogin.setStatusBar(self.statusbar)

        self.retranslateUi(TelaLogin)
        QtCore.QMetaObject.connectSlotsByName(TelaLogin)

    def retranslateUi(self, TelaLogin):
        _translate = QtCore.QCoreApplication.translate
        TelaLogin.setWindowTitle(_translate("TelaLogin", "MainWindow"))
        self.user.setText(_translate("TelaLogin", "Usuário"))
        self.passWord.setText(_translate("TelaLogin", "CPF"))
        self.btn_entrar.setText(_translate("TelaLogin", "Entrar"))
        self.no_conta.setText(_translate("TelaLogin", "Não tenho conta:"))
        self.btn_criar_conta.setText(_translate("TelaLogin", "Criar conta"))
        self.user_2.setText(_translate("TelaLogin", "LOGIN"))
