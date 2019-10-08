import ClasseProduto
from datetime import date, datetime

from BDVenda import BDvenda


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