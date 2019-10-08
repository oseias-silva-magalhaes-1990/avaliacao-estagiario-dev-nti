from PyQt5 import QtCore, QtGui, QtWidgets

from ClasseProduto import Produto
from TelaMensagem import Mensagem

class CadastrarProduto(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.cadastrar)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(547, 389)
        Form.setWindowIcon(QtGui.QIcon("img/icone.png"))

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 110, 191, 20))
        self.lineEdit.setObjectName("lineEdit")

        fontLabel = QtGui.QFont()
        fontLabel.setFamily("Arial")
        fontLabel.setPointSize(12)
        fontLabel.setBold(True)
        fontLabel.setWeight(75)

        self.labelErro = QtWidgets.QLabel(Form)
        self.labelErro.setGeometry(QtCore.QRect(40, 20, 520, 25))
        self.labelErro.setObjectName("labelErro")
        self.labelErro.setFont(fontLabel)
        self.labelErro.setStyleSheet('QLabel {color: red}')

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 90, 47, 13))
        self.label.setObjectName("label")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 180, 191, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 47, 13))
        self.label_2.setObjectName("label_Qtd")

        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 250, 191, 20))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 230, 61, 16))
        self.label_3.setObjectName("label_Val")

        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 320, 191, 20))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 300, 71, 16))
        self.label_4.setObjectName("label_4")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(404, 109, 101, 23))
        self.pushButton.setObjectName("Cadastrar")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(404, 179, 101, 23))
        self.pushButton_2.setObjectName("LimparCampos")

        self.pushButton.clicked.connect(self.copiarCampos)
        self.pushButton_2.clicked.connect(self.limparCampos)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastrar Produto"))
        self.label.setText(_translate("Form", "Codigo:"))
        self.label_2.setText(_translate("Form", "Nome:"))
        self.label_3.setText(_translate("Form", "Quantidade:"))
        self.label_4.setText(_translate("Form", "Valor Unitario:"))
        self.pushButton.setText(_translate("Form", "Cadastrar"))
        self.pushButton_2.setText(_translate("Form", "Limpar Campos"))

    def limparCampos(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.labelErro.clear()

    def copiarCampos(self):
        self.lineEdit.copy()
        self.lineEdit_2.copy()
        self.lineEdit_3.copy()
        self.lineEdit_4.copy()

    def cadastrar(self):
        codigo = self.lineEdit.text()
        nome = self.lineEdit_2.text()
        quantidade = self.lineEdit_3.text()
        valorUnitario = self.lineEdit_4.text()

        produto = Produto()
        if codigo and nome and quantidade and valorUnitario:
            if not produto.validaCodigo(codigo):
                produto.setCodigo(codigo)
                produto.setNome(nome)
                produto.setQuantidade(quantidade)
                produto.setValorUnit(valorUnitario)
                produto.gravaProduto()
                Mensagem.msg ='Produto cadastrado com sucesso!'
                Mensagem.cor = 'blue'
                self.switch_window.emit()
                self.limparCampos()
            else:
                self.labelErro.setText("Este código já está cadastrado!")
        else:
            self.labelErro.clear()



