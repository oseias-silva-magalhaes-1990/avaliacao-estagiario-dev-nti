from BDProduto import BDproduto

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