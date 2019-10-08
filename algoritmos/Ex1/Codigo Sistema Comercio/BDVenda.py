import pymysql

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
