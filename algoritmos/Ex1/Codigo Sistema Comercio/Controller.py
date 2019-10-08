from PyQt5 import QtCore, QtGui, QtWidgets
from TelaVenda import TelVenda
from TelaMensagem import Mensagem
from TelaMenuPrincipal import MenuPrincipal
from TelaCadastrarProduto import CadastrarProduto
import sys




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
