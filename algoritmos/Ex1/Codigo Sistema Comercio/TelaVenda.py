from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date, datetime

from ClasseProduto import Produto
from ClasseVenda import Venda
from TelaMensagem import Mensagem


class TelVenda(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()
    contCampos = 5

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton_Calcular.clicked.connect(self.calcularVenda)
        self.pushButton_CVenda.clicked.connect(self.confirmarVenda)
        self.pushButtonMaisCampos.clicked.connect(self.aumentaCampo)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 389)
        Form.setWindowIcon(QtGui.QIcon("img/icone.png"))

        self.ItensVendidos = QtWidgets.QScrollArea(Form)
        self.ItensVendidos.setGeometry(QtCore.QRect(10, 30, 380, 361))
        self.ItensVendidos.setWidgetResizable(False)
        self.ItensVendidos.setObjectName("ItensVendidos")

        fontLabel = QtGui.QFont()
        fontLabel.setFamily("Arial")
        fontLabel.setPointSize(9)
        fontLabel.setBold(True)
        fontLabel.setWeight(75)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 350, 899))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.lineProduto_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineProduto_4.setGeometry(QtCore.QRect(10, 120, 121, 21))
        self.lineProduto_4.setObjectName("lineProduto_4")

        self.lineQuantidade_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineQuantidade_4.setGeometry(QtCore.QRect(140, 120, 61, 21))
        self.lineQuantidade_4.setObjectName("lineQuantidade_4")

        self.lineQuantidade_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineQuantidade_3.setGeometry(QtCore.QRect(140, 90, 61, 21))
        self.lineQuantidade_3.setObjectName("lineQuantidade_3")

        self.lineProduto_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineProduto_1.setGeometry(QtCore.QRect(10, 30, 121, 21))
        self.lineProduto_1.setObjectName("lineProduto_1")

        self.lineProduto_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineProduto_2.setGeometry(QtCore.QRect(10, 60, 121, 21))
        self.lineProduto_2.setObjectName("lineProduto_2")

        self.lineProduto_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineProduto_6.setGeometry(QtCore.QRect(10, 180, 121, 21))
        self.lineProduto_6.setObjectName("lineProduto_6")
        self.lineProduto_6.setVisible(False)

        self.lineProduto_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineProduto_7.setGeometry(QtCore.QRect(10, 210, 121, 21))
        self.lineProduto_7.setObjectName("lineProduto_6")
        self.lineProduto_7.setVisible(False)

        self.lineQuantidade_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineQuantidade_5.setGeometry(QtCore.QRect(140, 150, 61, 21))
        self.lineQuantidade_5.setObjectName("lineQuantidade_5")

        self.lineQuantidade_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineQuantidade_1.setGeometry(QtCore.QRect(140, 30, 61, 21))
        self.lineQuantidade_1.setObjectName("lineQuantidade_1")

        self.lineQuantidade_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineQuantidade_6.setGeometry(QtCore.QRect(140, 180, 61, 21))
        self.lineQuantidade_6.setObjectName("lineQuantidade_2")
        self.lineQuantidade_6.setVisible(False)

        self.lineQuantidade_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineQuantidade_7.setGeometry(QtCore.QRect(140, 210, 61, 21))
        self.lineQuantidade_7.setObjectName("lineQuantidade_2")
        self.lineQuantidade_7.setVisible(False)

        self.lineValor_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineValor_3.setGeometry(QtCore.QRect(210, 90, 61, 21))
        self.lineValor_3.setObjectName("lineValor_3")
        self.lineValor_3.setReadOnly(True)

        self.lineValor_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineValor_4.setGeometry(QtCore.QRect(210, 120, 61, 21))
        self.lineValor_4.setObjectName("lineValor_4")
        self.lineValor_4.setReadOnly(True)

        self.lineValor_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineValor_6.setGeometry(QtCore.QRect(210, 180, 61, 21))
        self.lineValor_6.setObjectName("lineValor_6")
        self.lineValor_6.setReadOnly(True)
        self.lineValor_6.setVisible(False)

        self.lineValor_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineValor_7.setGeometry(QtCore.QRect(210, 210, 61, 21))
        self.lineValor_7.setObjectName("lineValor_6")
        self.lineValor_7.setReadOnly(True)
        self.lineValor_7.setVisible(False)

        self.lineProduto_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineProduto_3.setGeometry(QtCore.QRect(10, 90, 121, 21))
        self.lineProduto_3.setObjectName("lineProduto_3")

        self.label_Val = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_Val.setGeometry(QtCore.QRect(210, 10, 31, 16))
        self.label_Val.setObjectName("label_Val")

        self.label_ValDesc = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_ValDesc.setGeometry(QtCore.QRect(283, 10, 70, 16))
        self.label_ValDesc.setObjectName("label_ValDesc")

        self.lineValor_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineValor_5.setGeometry(QtCore.QRect(210, 150, 61, 21))
        self.lineValor_5.setObjectName("lineValor_5")
        self.lineValor_5.setReadOnly(True)

        self.label_Qtd = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_Qtd.setGeometry(QtCore.QRect(140, 10, 61, 16))
        self.label_Qtd.setObjectName("label_Qtd")

        self.lineQuantidade_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineQuantidade_2.setGeometry(QtCore.QRect(140, 60, 61, 21))
        self.lineQuantidade_2.setObjectName("lineQuantidade_2")

        self.lineValor_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineValor_2.setGeometry(QtCore.QRect(210, 60, 61, 21))
        self.lineValor_2.setObjectName("lineValor_2")
        self.lineValor_2.setReadOnly(True)

        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 10, 100, 13))
        self.label.setObjectName("CodProduto")

        self.lineValor_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineValor_1.setGeometry(QtCore.QRect(210, 30, 61, 21))
        self.lineValor_1.setObjectName("lineValor_1")
        self.lineValor_1.setReadOnly(True)

        self.lineValorDesc_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineValorDesc_1.setGeometry(QtCore.QRect(281, 30, 61, 21))
        self.lineValorDesc_1.setObjectName("lineValor_1")
        self.lineValorDesc_1.setReadOnly(True)

        self.lineValorDesc_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineValorDesc_2.setGeometry(QtCore.QRect(281, 60, 61, 21))
        self.lineValorDesc_2.setObjectName("lineValor_2")
        self.lineValorDesc_2.setReadOnly(True)

        self.lineValorDesc_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineValorDesc_3.setGeometry(QtCore.QRect(281, 90, 61, 21))
        self.lineValorDesc_3.setObjectName("lineValor_3")
        self.lineValorDesc_3.setReadOnly(True)

        self.lineValorDesc_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineValorDesc_4.setGeometry(QtCore.QRect(281, 120, 61, 21))
        self.lineValorDesc_4.setObjectName("lineValor_4")
        self.lineValorDesc_4.setReadOnly(True)

        self.lineValorDesc_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineValorDesc_5.setGeometry(QtCore.QRect(281, 150, 61, 21))
        self.lineValorDesc_5.setObjectName("lineValor_5")
        self.lineValorDesc_5.setReadOnly(True)

        self.lineValorDesc_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineValorDesc_6.setGeometry(QtCore.QRect(281, 180, 61, 21))
        self.lineValorDesc_6.setObjectName("lineValor_6")
        self.lineValorDesc_6.setReadOnly(True)
        self.lineValorDesc_6.setVisible(False)

        self.lineValorDesc_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineValorDesc_7.setGeometry(QtCore.QRect(281, 210, 61, 21))
        self.lineValorDesc_7.setObjectName("lineValor_6")
        self.lineValorDesc_7.setReadOnly(True)
        self.lineValorDesc_7.setVisible(False)

        self.lineProduto_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineProduto_5.setGeometry(QtCore.QRect(10, 150, 121, 21))
        self.lineProduto_5.setObjectName("lineProduto_5")

        self.pushButtonMaisCampos = QtWidgets.QPushButton(Form)
        self.pushButtonMaisCampos.setGeometry(QtCore.QRect(400, 29, 21, 23))
        self.pushButtonMaisCampos.setObjectName("pushButtonMaisCampos")
        self.pushButtonMaisCampos.setToolTip("Clique para adicionar mais campos")


        self.ItensVendidos.setWidget(self.scrollAreaWidgetContents)

        self.lineEdit_Desconto = QtWidgets.QLineEdit(Form)
        self.lineEdit_Desconto.setGeometry(QtCore.QRect(490, 150, 61, 20))
        self.lineEdit_Desconto.setObjectName("lineEdit_Desconto")

        self.label_Desc = QtWidgets.QLabel(Form)
        self.label_Desc.setGeometry(QtCore.QRect(430, 150, 47, 13))
        self.label_Desc.setObjectName("label_Desc")

        self.lineEdit_VTotal = QtWidgets.QLineEdit(Form)
        self.lineEdit_VTotal.setGeometry(QtCore.QRect(490, 180, 61, 20))
        self.lineEdit_VTotal.setObjectName("lineEdit_VTotal")

        self.label_Vtot = QtWidgets.QLabel(Form)
        self.label_Vtot.setGeometry(QtCore.QRect(430, 180, 61, 20))
        self.label_Vtot.setObjectName("label_Vtot")

        self.pushButton_CVenda = QtWidgets.QPushButton(Form)
        self.pushButton_CVenda.setGeometry(QtCore.QRect(490, 300, 61, 23))
        self.pushButton_CVenda.setObjectName("pushButton_CVenda")
        self.pushButton_CVenda.setVisible(False)

        self.label_ConfVenda = QtWidgets.QLabel(Form)
        self.label_ConfVenda.setGeometry(QtCore.QRect(400, 300, 91, 20))
        self.label_ConfVenda.setObjectName("label_ConfVenda")
        self.label_ConfVenda.setVisible(False)


        self.pushButton_Calcular = QtWidgets.QPushButton(Form)
        self.pushButton_Calcular.setGeometry(QtCore.QRect(490, 120, 61, 23))
        self.pushButton_Calcular.setObjectName("pushButton_Calcular")

        self.label_CalcVenda = QtWidgets.QLabel(Form)
        self.label_CalcVenda.setGeometry(QtCore.QRect(410, 120, 81, 20))
        self.label_CalcVenda.setObjectName("label_CalcVenda")

        self.label_dh = QtWidgets.QLabel(Form)
        self.label_dh.setGeometry(QtCore.QRect(450, 10, 100, 40))
        self.label_dh.setAlignment(QtCore.Qt.AlignRight)
        self.label_dh.setObjectName("label_dh")

        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 270, 16))
        self.label_9.setFont(fontLabel)
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Form)
        self.pushButton_Calcular.clicked.connect(self.lineProduto_1.copy)
        self.pushButton_Calcular.clicked.connect(self.lineProduto_2.copy)
        self.pushButton_Calcular.clicked.connect(self.lineProduto_3.copy)
        self.pushButton_Calcular.clicked.connect(self.lineProduto_4.copy)
        self.pushButton_Calcular.clicked.connect(self.lineProduto_5.copy)
        self.pushButton_Calcular.clicked.connect(self.lineQuantidade_1.copy)
        self.pushButton_Calcular.clicked.connect(self.lineQuantidade_2.copy)
        self.pushButton_Calcular.clicked.connect(self.lineQuantidade_3.copy)
        self.pushButton_Calcular.clicked.connect(self.lineQuantidade_4.copy)
        self.pushButton_Calcular.clicked.connect(self.lineQuantidade_5.copy)
        self.pushButton_Calcular.clicked.connect(self.lineValor_1.copy)
        self.pushButton_Calcular.clicked.connect(self.lineValor_2.copy)
        self.pushButton_Calcular.clicked.connect(self.lineValor_3.copy)
        self.pushButton_Calcular.clicked.connect(self.lineValor_4.copy)
        self.pushButton_Calcular.clicked.connect(self.lineValor_5.copy)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sistema Comercial"))
        self.label_Val.setText(_translate("Form", "Valor"))
        self.label_ValDesc.setText(_translate("Form", "Valor c/ Desc."))
        self.label_Qtd.setText(_translate("Form", "Quantidade"))
        self.label.setText(_translate("Form", "Codigo do Produto"))
        self.pushButtonMaisCampos.setText(_translate("Form", "+"))
        self.label_Desc.setText(_translate("Form", "Desconto:"))
        self.label_Vtot.setText(_translate("Form", "Valor Total:"))
        self.pushButton_CVenda.setText(_translate("Form", "OK"))
        self.label_ConfVenda.setText(_translate("Form", "Confirmar Venda?"))
        self.pushButton_Calcular.setText(_translate("Form", "Calcular"))
        self.label_CalcVenda.setText(_translate("Form", "Calcular Venda?"))
        self.label_dh.setText(_translate("Form", datetime.today().strftime('%d/%m/%Y\n%H:%M')))

    def limparCampos(self):
        self.lineEdit_VTotal.clear()
        self.lineEdit_Desconto.clear()

        self.lineProduto_1.clear()
        self.lineProduto_2.clear()
        self.lineProduto_3.clear()
        self.lineProduto_4.clear()
        self.lineProduto_5.clear()
        self.lineProduto_6.clear()
        self.lineProduto_7.clear()

        self.lineQuantidade_1.clear()
        self.lineQuantidade_2.clear()
        self.lineQuantidade_3.clear()
        self.lineQuantidade_4.clear()
        self.lineQuantidade_5.clear()
        self.lineQuantidade_6.clear()
        self.lineQuantidade_7.clear()

        self.lineValor_1.clear()
        self.lineValor_2.clear()
        self.lineValor_3.clear()
        self.lineValor_4.clear()
        self.lineValor_5.clear()
        self.lineValor_6.clear()
        self.lineValor_7.clear()

        self.lineValorDesc_1.clear()
        self.lineValorDesc_2.clear()
        self.lineValorDesc_3.clear()
        self.lineValorDesc_4.clear()
        self.lineValorDesc_5.clear()
        self.lineValorDesc_6.clear()
        self.lineValorDesc_7.clear()

    def aumentaCampo(self):
        if TelVenda.contCampos == 5:
            self.lineProduto_6.setVisible(True)
            self.lineQuantidade_6.setVisible(True)
            self.lineValor_6.setVisible(True)
            self.lineValorDesc_6.setVisible(True)
            TelVenda.contCampos += 1
            return None
        if TelVenda.contCampos == 6:
            self.lineProduto_7.setVisible(True)
            self.lineQuantidade_7.setVisible(True)
            self.lineValor_7.setVisible(True)
            self.lineValorDesc_7.setVisible(True)
            TelVenda.contCampos += 1
            return None
        if TelVenda.contCampos == 7:
            self.label_9.setText("LIMITE MÀXIMO DE CAMPOS!")

    def carregaValores(self):
        self.cod = [self.lineProduto_1.text(),
                    self.lineProduto_2.text(),
                    self.lineProduto_3.text(),
                    self.lineProduto_4.text(),
                    self.lineProduto_5.text(),
                    self.lineProduto_6.text(),
                    self.lineProduto_7.text()]
        print("Codigos:")
        print(self.cod)

        self.qtd = [(self.lineQuantidade_1.text()),
                    (self.lineQuantidade_2.text()),
                    (self.lineQuantidade_3.text()),
                    (self.lineQuantidade_4.text()),
                    (self.lineQuantidade_5.text()),
                    (self.lineQuantidade_6.text()),
                    (self.lineQuantidade_7.text())]
        print("Quantidades: ")
        print(self.qtd)

    def escreveValor(self, indice):
        if indice == 0:
            self.lineValor_1.setText(str(self.produto.getValorUnitario()))
            self.val.append(self.lineValor_1.text())
        if indice == 1:
            self.lineValor_2.setText(str(self.produto.getValorUnitario()))
            self.val.append(self.lineValor_2.text())
        if indice == 2:
            self.lineValor_3.setText(str(self.produto.getValorUnitario()))
            self.val.append(self.lineValor_3.text())
        if indice == 3:
            self.lineValor_4.setText(str(self.produto.getValorUnitario()))
            self.val.append(self.lineValor_4.text())
        if indice == 4:
            self.lineValor_5.setText(str(self.produto.getValorUnitario()))
            self.val.append(self.lineValor_5.text())
        if indice == 5:
            self.lineValor_6.setText(str(self.produto.getValorUnitario()))
            self.val.append(self.lineValor_6.text())
        if indice == 6:
            self.lineValor_7.setText(str(self.produto.getValorUnitario()))
            self.val.append(self.lineValor_7.text())

    def escreveValorDesc(self, indice):
        if indice == 0:
            self.lineValorDesc_1.setText(str(self.valorDesc[indice]))
        if indice == 1:
            self.lineValorDesc_2.setText(str(self.valorDesc[indice]))
        if indice == 2:
            self.lineValorDesc_3.setText(str(self.valorDesc[indice]))
        if indice == 3:
            self.lineValorDesc_4.setText(str(self.valorDesc[indice]))
        if indice == 4:
            self.lineValorDesc_5.setText(str(self.valorDesc[indice]))
        if indice == 5:
            self.lineValorDesc_6.setText(str(self.valorDesc[indice]))
        if indice == 6:
            self.lineValorDesc_7.setText(str(self.valorDesc[indice]))

    def calcularVenda(self):
        self.carregaValores()
        self.produto = Produto()
        indCodErrado = None
        desconto=[]
        somaDescontos = 0.0
        self.valorTotal = 0.0
        self.val = []
        self.valorDesc=[]
        self.antVazio = False

        for indice in range(len(self.cod)):
            if indice > 0 and self.cod[indice] != '':
                if self.cod[indice - 1] == '':
                    self.antVazio = True

        if self.antVazio == False:
            self.label_9.clear()
            for indice in range(len(self.cod)):
                if self.cod[indice] and self.qtd[indice]:
                    if self.produto.validaCodigo(str(self.cod[indice])):
                        self.produto.recuperaProduto(self.cod[indice])
                        if int(self.produto.getQuantidade()) > int(self.qtd[indice]):
                            self.escreveValor(indice)
                            desconto.append(self.produto.obtemDesconto(int(self.qtd[indice])))
                            somaDescontos += float(desconto[indice])*100
                            self.valorTotal += int(self.qtd[indice])*(float(self.val[indice]) - float(self.val[indice])*desconto[indice])
                            self.valorDesc.append(int(self.qtd[indice])*(float(self.val[indice]) - float(self.val[indice])*desconto[indice]))
                            self.escreveValorDesc(indice)
                            self.pushButton_CVenda.setVisible(True)
                            self.label_ConfVenda.setVisible(True)
                        else:
                            self.label_9.setText("Quantidade do codigo "+self.cod[indice]+" maior que o estoque")
                            return None
                    else:
                        indCodErrado = indice
        else:
            self.label_9.setText("Preencha os campos na sequência correta!")
            self.label_9.setStyleSheet('QLabel {color: red}')
            self.pushButton_CVenda.setVisible(False)
            self.label_ConfVenda.setVisible(False)

        if indCodErrado == None:
            print("valor Total: " + str(self.valorTotal))
            print("Desconto: " + str(somaDescontos))
            self.lineEdit_VTotal.setText(str(self.valorTotal))
            self.lineEdit_Desconto.setText(str(somaDescontos)+'%')
        else:
            self.label_9.setText('O código '+str(self.cod[indCodErrado])+' não está cadastrado!')
            self.label_9.setStyleSheet('QLabel {color: red}')

    def atualizaQtdEstoque(self, cod, qtd):
        qtd = int(self.produto.getQuantidade()) - int(qtd)
        self.produto.atualizaQuantidade(str(cod), str(qtd))

    def confirmarVenda(self):
        self.itensVendidos =''
        for pos in range(len(self.cod)):
            if self.cod[pos] and self.qtd[pos]:
                self.itensVendidos += '('+str(self.cod[pos])+','+str(self.qtd[pos]+','+str(self.valorDesc[pos])+'),')
                self.atualizaQtdEstoque(self.cod[pos], self.qtd[pos])
        self.itensVendidos += str(self.valorTotal)
        print(self.itensVendidos)
        venda = Venda()
        venda.setItensVendidos(self.itensVendidos)
        venda.gravaVenda()
        self.limparCampos()
        Mensagem.msg = "VENDA CONCLUÍDA COM SUCESSO!"
        Mensagem.cor = 'blue'
        self.switch_window.emit()