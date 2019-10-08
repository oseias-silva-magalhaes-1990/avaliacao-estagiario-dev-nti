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