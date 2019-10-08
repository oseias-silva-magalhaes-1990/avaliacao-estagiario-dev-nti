from PyQt5 import QtCore, QtGui, QtWidgets


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