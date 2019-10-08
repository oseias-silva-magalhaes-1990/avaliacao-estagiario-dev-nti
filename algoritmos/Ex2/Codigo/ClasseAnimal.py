class Animal(object):
	
	def __init__(self):
		self.peso = 1.00
		self.qtdPatas = 0

	def inserirQtdPatas(self, qtdPatas):
		self.qtdPatas = qtdPatas

	def inserirPeso(self, peso):
		self.peso = peso

	def obterQtdPatas(self):
		return self.qtdPatas

	def obterPeso(self):
		return self.peso

	def andar(self):
		return 'estou andando'

	def correr(self):
		return 'estou correndo'

	def comer(self):
		return 'estou comendo'

	def dormir(self):
		return 'estou dormindo'

	def acordar(self):
		return 'estou acordado'

	def parar(self):
		return 'estou parado'




	
