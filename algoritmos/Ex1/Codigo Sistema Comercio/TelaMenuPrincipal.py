from PyQt5 import QtCore, QtGui, QtWidgets


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