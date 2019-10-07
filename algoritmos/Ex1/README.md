Neste exercío tentei utilizar o máximo de conhecimento possível em tempo oportuno para que houvesse tempo de resolução dos demais 
exercicios.
Criei um banco de dados denominado comercio que possui duas tabelas venda e produto.
Utilizando o MySQL Workbench desenvolvi as tabelas abaixo:
#Criando o banco
 CREATE DATABASE comercio;

#Criando a tabela produto
 CREATE TABLE `produto` (
  `id_produto` int(10) NOT NULL,
  `codigo` int(10) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `valorUnitario` decimal(14,2) NOT NULL,
  `quantidade` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#Definindo id_produto como chave primária
ALTER TABLE `produto`
  ADD PRIMARY KEY (`id_produto`);
  
#Definindo id_produto como auto-increment
ALTER TABLE `produto`
  MODIFY `id_produto` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
  
 #Criando a tabela venda
 CREATE TABLE `venda` (
  `numero` int(10) NOT NULL,
  `dhVenda` datetime NOT NULL,
  `itensVendidos` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#Definindo numero como chave primária
ALTER TABLE `venda`
  ADD PRIMARY KEY (`numero`);

#Definindo numero como auto_increment
ALTER TABLE `venda`
  MODIFY `numero` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

Utilizei a Linguagem Python como ferramenta para desenvolvimento orientado a on=bjeto das classes e interfaces do sistema de comércio.
Criei as classes BDProduto, BDVenda, Venda, Produto, TelaVenda, TelaCadastro, TelaMensagem, MenuPrincipal, Controller.
Trabalhi utilizando algumas validações de banco para verificar se por exemplo um produto já estava cadastrado, verificar se um 
produto a ser vendido existia no sistema, e para cada caso específico mostrando uma mensagem de erro ou alerta para o usuário.
Passando a concluir a venda apenas quando todos os requisitos fossem atendidos, e os eventuais erros corrigidos.

Na classe TelaMenuPrincipal criei dois botões sendo um Vender e outro Cadastrar, onde pode-se alternar entre as janelas mantendo as 
mesmas abertas ao mesmo tempo.
Todo Cadastro é registrado na tabela cadastro do banco de dados comercio e armazena o código do produto, nome, valor unitário e a 
quantidade.
Para realização dos testes durante o desenvolvmento, foi necessário inserir alguns produtos como pode ser visto abaixo:

Ex.:
INSERT INTO `produto` (`id_produto`, `codigo`, `nome`, `valorUnitario`, `quantidade`) VALUES
(1, 1, 'tv32', '1000.00', 935),
(2, 2, 'tv42', '2000.00', 946),
(3, 3, 'tv50pol', '3000.00', 990),
(4, 4, 'tv20pol', '4000.00', 990),
(5, 5, 'tv29', '5000.00', 990),
(6, 6, 'tv46', '25250.00', 25630),
(7, 7, 'somPortátil', '125.00', 560),
(8, 10, 'radio', '256.25', 9);


Toda venda realizada é salva na tabela venda, com os dados de hora e data da venda, e uma coluna itensVendidos do tipo longtext recebe
concatenado uma sequência de valores como observa-se abaixo:
O número da venda registrado é auto-incremento que varia a cada inserção, e é único cabendo no cenário deste sistema de comércio.
dhVenda = datetime.current()
itensVendidos += (codigo, quantidade, valor com desconto),...,(codigo, quantidade, valor com desconto),valor total

Ex.:
INSERT INTO `venda` (`numero`, `dhVenda`, `itensVendidos`) VALUES
(1, '2019-10-07 14:02:00', '(1,2,2000.0),2000.0'),
(2, '2019-10-07 14:03:00', '(2,10,20000.0),(1,5,5000.0),25000.0'),
(3, '2019-10-07 14:04:00', '(1,10,10000.0),(2,5,10000.0),20000.0'),
(4, '2019-10-07 14:11:00', '(10,1,256.25),256.25'),
(5, '2019-10-07 14:22:00', '(1,2,2000.0),2000.0');

Para cada produto que é vendido a venda é registrada e o produto é dcrementado do estoque, sendo atualizado a tabela dos produtos a cada
venda realizada.
Para fins de testes rápido sem a necessidade do editor, disponibilizei também um arquivo executável o qual tem sua funcionalidade
idependente.

Na tela de venda foram despostos alguns campos para a entrada dos dados, sendo Codigo e Quantidade os únicos valores a serem digitados
para efetuação de uma venda, após a inserção dos valores nos campos o usuário clica no botão calcular, assim os campos são preenchidos
com os valores já cadastrados pertencentes ao código do produto digitado e a tela de venda também possui os campos para inserir os 
valores calculados com desconto para cada produto. Também estão dispostos dois campos que após calcular mostram o total de descontos 
obtidos e o valor total da venda. Após calcular o botão para finalização da compra se torna visível ao usuário e este pode concluir a 
venda.

A tela de Cadastro visa ser simples não incluíndo outras funcionalidades além do cadastro do produto no banco, sendo dispostos os 
para a entrada dos dados do produto e uma verificação de banco para saber de o produto à ser cadastrado já existe no sistema.

A tela mensagem aparece para finalizar as vendas e os cadastros, mostrando um mensagem de confirmação com um botão de ok.
Foram utilizadas as bibliotecas PyQt5 para as interfaces gráficas, a datetime, a sys, e pymysql para a comunicação entre o sistema e o
banco de dados.
A seguir está disposto o script completo do código do sistema:

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date, datetime
import sys
import pymysql

class BDproduto(object):

    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "", "comercio")
        self.cursor = self.db.cursor()

    def gravaBDproduto(self, codigo, nome, valorUnitario, quantidade):
        dados = (codigo, nome, valorUnitario, quantidade)
        self.cursor.execute("INSERT INTO produto(codigo, nome, valorUnitario, quantidade) VALUES (%s, %s, %s, %s)", dados)
        self.db.commit()
        self.db.close()

    def atualizaNome(self, codigo, nome):
        dados = (nome, codigo)
        self.cursor.execute("UPDATE produto SET nome = %s WHERE codigo = %s", dados)
        self.db.commit()
        self.db.close()

    def atualizaValorUnitario(self, codigo, valorUnitario):
        dados = (valorUnitario, codigo)
        self.cursor.execute("UPDATE produto SET valorUnitario = %s WHERE codigo = %s", dados)
        self.db.commit()
        self.db.close()

    def atualizaQuantidade(self, codigo, quantidade):
        dados = (quantidade, codigo)
        self.cursor.execute("UPDATE produto SET quantidade = %s WHERE codigo = %s", dados)
        self.db.commit()
        self.db.close()

    def recuperaBDproduto(self, codigo):
        self.cursor.execute("SELECT * FROM produto WHERE codigo = %s", codigo)
        dado = self.cursor.fetchall()
        self.db.close()
        return dado

    def validaBDcodigo(self, codigo):
        self.cursor.execute("SELECT codigo FROM produto WHERE codigo = %s", codigo)
        dado = self.cursor.fetchone()
        self.db.close()
        if not dado:
            return False
        else:
            return True

#================================================================================================================================
#================================================================================================================================

class BDvenda(object):

    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "", "comercio")
        self.cursor = self.db.cursor()

    def gravaBDvenda(self, dhVenda, itensVendidos):
        dados = (dhVenda, itensVendidos)
        self.cursor.execute("INSERT INTO venda(dhVenda, itensVendidos) VALUES (%s, %s)", dados)
        self.db.commit()
        self.db.close()

    def recuperaBDvenda(self, numero):
        self.cursor.execute("SELECT * FROM venda WHERE numero = %s", numero)
        dado = self.cursor.fetchall()
        self.db.close()
        return dado

    def atualizaDHvenda(self, numero, dhVenda):
        dados = (dhVenda, numero)
        self.cursor.execute("UPDATE item SET dhVenda = %s WHERE numero = %s", dados)
        self.db.commit()
        self.db.close()

    def atualizaItensVendidos(self, numero, itensVendidos):
        dados = (itensVendidos, numero)
        self.cursor.execute("UPDATE item SET itensVendidos = %s WHERE numero = %s", dados)
        self.db.commit()
        self.db.close()

    def validaBDvenda(self, numero):
        self.cursor.execute("SELECT id FROM venda WHERE numero = %s", numero)
        dado = self.cursor.fetchone()
        self.db.close()
        if not dado:
            return False
        else:
            return True


#================================================================================================================================
#================================================================================================================================


class Produto(object):
    def __init_(self, codigo, nome, valorUnitario, quantidade):
        self.idProduto = 0
        self.codigo = codigo
        self.nome = nome
        self.valorUnitario = valorUnitario
        self.quantidade = quantidade
        self.desconto = 0

    def setCodigo(self, codigo):
        self.codigo = codigo

    def setNome(self, nome):
        self.nome = nome

    def setValorUnit(self, valorUnitario):
        self.valorUnitario = valorUnitario

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade

    def getCodigo(self):
        return self.codigo

    def getNome(self):
        return self.nome

    def getValorUnitario(self):
        return self.valorUnitario

    def getQuantidade(self):
        return self.quantidade

    def getIDproduto(self):
        return self.idProduto

    def validaCodigo(self, codigo):
        dbProd = BDproduto()
        return dbProd.validaBDcodigo(codigo)

    def obtemDesconto(self, qtd):
        if qtd <= 10:
            self.desconto = 0
            return self.desconto
        if qtd > 10 and qtd < 20:
            self.desconto = 0.05
            return self.desconto
        if qtd >= 20 and qtd < 30:
            self.desconto = 0.1
            return self.desconto
        if qtd >= 30:
            self.desconto = 0.2
            return self.desconto

    def recuperaProduto(self, codigo):
        dbProd = BDproduto()
        produto = dbProd.recuperaBDproduto(codigo)
        self.idProduto = produto[0][0]
        self.codigo = produto[0][1]          
        self.nome = produto[0][2]
        self.valorUnitario = produto[0][3]
        self.quantidade = produto[0][4]

    def gravaProduto(self):
        dbProd = BDproduto()
        dbProd.gravaBDproduto(self.codigo, self.nome, self.valorUnitario, self.quantidade)

    def atualizaQuantidade(self, cod, qtd):
        dbProd = BDproduto()
        dbProd.atualizaQuantidade(cod, qtd)

#================================================================================================================================
#================================================================================================================================

class Venda(object):

    def __init_(self):
        self.numero = 0
        self.itensVendidos = ''

    def setItensVendidos(self, itensVendidos):
        self.itensVendidos = itensVendidos

    def getNumeroVenda(self):
        return self.numero

    def getDHvenda(self):
        return self.dhVenda

    def recuperaVenda(self, numero):
        dbVenda = BDvenda()
        venda = dbVenda.recuperaBDvenda(numero)

    def gravaVenda(self):
        dbVenda = BDvenda()
        self.dhVenda = datetime.today().strftime("%Y-%m-%d %H:%M")
        print(self.dhVenda)
        dbVenda.gravaBDvenda(self.dhVenda, self.itensVendidos)

#================================================================================================================================
#================================================================================================================================

class Mensagem(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()
    msg = ''
    cor = ''

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.fechaJanela)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 255)
        Form.setWindowIcon(QtGui.QIcon("img/icone.png"))

        fontLabel = QtGui.QFont()
        fontLabel.setFamily("Arial")
        fontLabel.setPointSize(12)
        fontLabel.setBold(True)
        fontLabel.setWeight(75)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 19, 321, 101))
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label.setStyleSheet('QLabel {color:'+Mensagem.cor+'}')

        self.label.setFont(fontLabel)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 170, 75, 23))
        self.pushButton.setShortcut("")
        self.pushButton.setObjectName("pushButtonMaisCampos")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastrar Produto"))
        self.label.setText(_translate("Form", Mensagem.msg))
        self.pushButton.setText(_translate("Form", "OK"))

    def fechaJanela(self):
        self.switch_window.emit()

#================================================================================================================================
#================================================================================================================================

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
        self.lineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+"), self.lineEdit))

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
        self.lineEdit_2.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z ]+"), self.lineEdit_2))

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 47, 13))
        self.label_2.setObjectName("label_Qtd")

        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 250, 191, 20))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+"), self.lineEdit_3))

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 230, 61, 16))
        self.label_3.setObjectName("label_Val")

        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 320, 191, 20))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+[.][0-9][0-9]"), self.lineEdit_4))

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

#================================================================================================================================
#================================================================================================================================

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



#================================================================================================================================
#================================================================================================================================

class MenuPrincipal(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.telaVender)
        self.pushButton_2.clicked.connect(self.telaCadastrar)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 255)
        Form.setWindowIcon(QtGui.QIcon("img/icone.png"))

        fontLabel = QtGui.QFont()
        fontLabel.setFamily("Arial")
        fontLabel.setPointSize(9)
        fontLabel.setBold(True)
        fontLabel.setWeight(75)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 60, 321, 20))
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label.setFont(fontLabel)

        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(10, 147, 321, 20))
        self.label_1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_1.setObjectName("label_1")
        self.label_1.setFont(fontLabel)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 75, 75, 23))
        self.pushButton.setShortcut("")
        self.pushButton.setObjectName("TelaVender")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 163, 75, 23))
        self.pushButton_2.setShortcut("")
        self.pushButton_2.setObjectName("TelaCadastrar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Menu - Sistema de Comércio"))
        self.label.setText(_translate("Form", "Vender"))
        self.label_1.setText(_translate("Form", "Cadastrar"))
        self.pushButton.setText(_translate("Form", "Vender"))
        self.pushButton_2.setText(_translate("Form", "Cadastrar"))

    def telaCadastrar(self):
        self.switch_window.emit()

    def telaVender(self):
        self.switch_window_2.emit()

#================================================================================================================================
#================================================================================================================================

class Controller:

    def __init__(self):
        pass

    def show_TVenda(self):
        self.venda = TelVenda()
        self.venda.switch_window.connect(self.show_Msg)
        self.venda.show()

    def show_TCadastra(self):
        self.cad = CadastrarProduto()
        self.cad.switch_window.connect(self.show_Msg)
        self.cad.show()

    def show_Msg(self):
        self.msg = Mensagem()
        self.msg.switch_window.connect(self.fecha_Msg)
        self.msg.show()

    def fecha_Msg(self):
        self.msg.close()

    def show_menuPrin(self):
        self.menuPrin = MenuPrincipal()
        self.menuPrin.switch_window.connect(self.show_TCadastra)
        self.menuPrin.switch_window_2.connect(self.show_TVenda)
        self.menuPrin.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_menuPrin()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()






