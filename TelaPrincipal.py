# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaInicial(object):
    def setupUi(self, TelaInicial):
        TelaInicial.setObjectName("TelaInicial")
        TelaInicial.resize(500, 866)
        font = QtGui.QFont()
        font.setPointSize(14)
        TelaInicial.setFont(font)
        TelaInicial.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(TelaInicial)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 481, 201))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(145, 65, 172);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(360, 70, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(145, 65, 172);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(145, 65, 172);")
        self.label_3.setObjectName("label_3")
        self.bnt_sair = QtWidgets.QPushButton(self.frame)
        self.bnt_sair.setGeometry(QtCore.QRect(368, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.bnt_sair.setFont(font)
        self.bnt_sair.setStyleSheet("\n"
"background-color: rgb(145, 65, 172);\n"
"\n"
"\n"
"color: rgb(255, 255, 255);")
        self.bnt_sair.setObjectName("bnt_sair")
        self.nomeUser = QtWidgets.QLabel(self.frame)
        self.nomeUser.setGeometry(QtCore.QRect(50, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nomeUser.setFont(font)
        self.nomeUser.setStyleSheet("color: rgb(145, 65, 172);")
        self.nomeUser.setObjectName("nomeUser")
        self.labelSaldo = QtWidgets.QLabel(self.frame)
        self.labelSaldo.setGeometry(QtCore.QRect(10, 120, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelSaldo.setFont(font)
        self.labelSaldo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelSaldo.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(192, 97, 203);")
        self.labelSaldo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSaldo.setObjectName("labelSaldo")
        self.labelNConta = QtWidgets.QLabel(self.frame)
        self.labelNConta.setGeometry(QtCore.QRect(370, 110, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelNConta.setFont(font)
        self.labelNConta.setStyleSheet("background-color: rgb(192, 97, 203);\n"
"color: rgb(255, 255, 255);")
        self.labelNConta.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNConta.setObjectName("labelNConta")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 240, 481, 361))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_transferir = QtWidgets.QPushButton(self.frame_2)
        self.btn_transferir.setGeometry(QtCore.QRect(30, 120, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_transferir.setFont(font)
        self.btn_transferir.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(145, 65, 172);")
        self.btn_transferir.setObjectName("btn_transferir")
        self.btn_Depositar = QtWidgets.QPushButton(self.frame_2)
        self.btn_Depositar.setGeometry(QtCore.QRect(320, 120, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Depositar.setFont(font)
        self.btn_Depositar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(145, 65, 172);")
        self.btn_Depositar.setObjectName("btn_Depositar")
        self.btn_sacar = QtWidgets.QPushButton(self.frame_2)
        self.btn_sacar.setGeometry(QtCore.QRect(30, 250, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_sacar.setFont(font)
        self.btn_sacar.setStyleSheet("color: rgb(145, 65, 172);\n"
"background-color: rgb(255, 255, 255);")
        self.btn_sacar.setObjectName("btn_sacar")
        self.btn_extrato = QtWidgets.QPushButton(self.frame_2)
        self.btn_extrato.setGeometry(QtCore.QRect(330, 250, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_extrato.setFont(font)
        self.btn_extrato.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(145, 65, 172);")
        self.btn_extrato.setObjectName("btn_extrato")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 610, 481, 241))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_historico = QtWidgets.QLabel(self.frame_3)
        self.label_historico.setGeometry(QtCore.QRect(180, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_historico.setFont(font)
        self.label_historico.setStyleSheet("color: rgb(192, 97, 203);")
        self.label_historico.setObjectName("label_historico")
        self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit.setGeometry(QtCore.QRect(40, 60, 401, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(145, 65, 172);\n"
"border-color: rgb(97, 53, 131);")
        self.textEdit.setObjectName("textEdit")
        TelaInicial.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TelaInicial)
        self.statusbar.setObjectName("statusbar")
        TelaInicial.setStatusBar(self.statusbar)

        self.retranslateUi(TelaInicial)
        QtCore.QMetaObject.connectSlotsByName(TelaInicial)

    def retranslateUi(self, TelaInicial):
        _translate = QtCore.QCoreApplication.translate
        TelaInicial.setWindowTitle(_translate("TelaInicial", "MainWindow"))
        self.label.setText(_translate("TelaInicial", "Seu saldo:"))
        self.label_2.setText(_translate("TelaInicial", "Nº da Conta:"))
        self.label_3.setText(_translate("TelaInicial", "Olá, "))
        self.bnt_sair.setText(_translate("TelaInicial", "Sair"))
        self.nomeUser.setText(_translate("TelaInicial", "NomeUser"))
        self.labelSaldo.setText(_translate("TelaInicial", "asdasds"))
        self.labelNConta.setText(_translate("TelaInicial", "000"))
        self.btn_transferir.setText(_translate("TelaInicial", "Transferir"))
        self.btn_Depositar.setText(_translate("TelaInicial", "Depositar"))
        self.btn_sacar.setText(_translate("TelaInicial", "Sacar"))
        self.btn_extrato.setText(_translate("TelaInicial", "Extrato"))
        self.label_historico.setText(_translate("TelaInicial", "Histórico"))